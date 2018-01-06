import re
import bs4
from markdown import markdown

# TODO: there is a problem with the javascript or css that is causing the href text to come to the front. 
# This is easily seen with the glossary example. How to fix this?

require_plugins = []

# Add in our javascript and style handling
include_in_header = "glossary.css"
include_after = "glossary.js"

class Term(object):
    def __init__(self, name, expansion, description):
        self.name = name
        self.expansion = expansion
        self.description = description

class GlossaryPlugin(object):

    def __init__(self, preprocessor):
        self.pp = preprocessor
        self.token = "glossary"
        self.pp.register_plugin(self)
        self.terms = {}
        self.glossid = 0
        self.visible = False

    def preprocess(self, s):
        """
        In this phase, all definition elements have been declared. Replace the glossary tags with the 
        full glossary.
        """
        return s.replace("<!-- INSERT GLOSSARY -->", self.glossary2html())

    def postprocess_soup(self, soup):
        """
        For each instance of a glossary word, replace it with a glossary tag
        """

        # Only run this if there is indeed a glossary
        if len(self.terms.keys()) == 0: return
        term_list = "|".join(self.terms)

        # TODO: there is at least one rendering issue with two glossary
        # elements inside an <em> block that is rendering wrong.

        # Only look in the main body, skip scripts, TOC, etc
        main = soup.find("div", {"id": "MAIN"})

        term_search = re.compile(r"^(|.*?[\s(\"'])(%s)(|[\s.?!\"',)].*)$" % term_list, re.MULTILINE)
        for string in list(main.strings):
            if string.parent.name == "code": continue # skip code fragments
            if string.parent.name == "a": continue # skip hyperlinks
            # TODO: can I do this smarter by explicitly tagging td elements for the dictionary? The code seems to work, 
            # though I want to make sure that this isn't hurting build perf.
            skipit = False
            for parent in string.parents:
                if parent == None: continue
                if parent.attrs == None: continue
                if parent.attrs.has_key("id") and parent.attrs["id"] == "table-glossary":
                    skipit = True
                    break
                if parent.attrs.has_key("class") and ("definition_popup" in parent.attrs["class"]):
                    # Skip hyperlinks for the popup windows
                    skipit = True
                    break
            if skipit: continue

            found_match = False
            text = unicode(string)
            while (True):
                m = term_search.search(text)
                if not m: break

                found_match = True
                string.insert_before(bs4.NavigableString(m.group(1)))
                # Replace the term search with the rest of the string so we can iterate on terms
                text = m.group(3)
                if self.visible:
                    ahref = soup.new_tag("a", href='#glossary_%s' % m.group(2))
                    ahref.string = m.group(2)
                    ahref.attrs["class"] = "glossary_link"
                    ahref.attrs["data-show"] ="define_%s" % m.group(2)
                    string.insert_before(ahref)
                else:
                    span = soup.new_tag("span")
                    span.string = m.group(2)
                    span.attrs["class"] = "glossary_link"
                    span.attrs["data-show"] ="define_%s" % m.group(2)
                    string.insert_before(span)

            if found_match:
                # Put whatever remains at the end and extract the original string
                string.insert_before(bs4.NavigableString(text))
                string.extract()

    def process(self, code, show=False, div_style=None):
        """
        Fill up our glossary with the terms defined.
        """
        # Remove illegal characters
        code = self.pp.cleanstr(code)

        # Parse out the terms, add to global dict and return whatever is new here.
        new_terms = self.parse_glossary(code)

        # Append invisible div's for the pop-ups
        s = "\n\n"
        if (len(new_terms.keys()) > 0):
            s += '<div id="glossary_popups%d">\n' % self.glossid
            for name in sorted(new_terms.keys()):
                term = new_terms[name]
                s += "<div class=\"definition_popup_arrow\" id=\"define_%sarrow\"></div>\n" % term.name
                s += "<div class=\"definition_popup\" id=\"define_%s\">\n" % term.name
                md2html = markdown(term.description.strip())
                # I want to remove containing <p> ... </p> if they are there alone. But if it is part of a more 
                # complex string, I want to leave them.
                if (re.search("<p>.*?</p>$", md2html)):
                    if md2html.startswith("<p>"): md2html = md2html[3:]
                    if md2html.endswith("</p>"): md2html = md2html[:-4]
                if (term.expansion != None):
                    # First add the expansion
                    s += "<b>%s</b><br>" % term.expansion
                s += md2html
                s += "</div>\n"
            s += "</div>\n"
            self.glossid += 1
            s += "\n\n"

        # Insert string for the glossary insertion, it will happen at a later phase.
        if (show):
            self.visible = True
            return s + "<!-- INSERT GLOSSARY -->"
        else:
            # Remove the glossary, the user just wanted to add these terms to the list.
            return s
    
    def parse_glossary(self, code):
        """
        Split into terms and definitions and return a dict with the results.

        Collect all glossary terms in the document, they will be printed later.
        """
        terms = re.split("\n==", code)
        new_terms = {}
        for term in terms:
            if term.strip() == "": continue
            lines = term.split("\n")
            term_name = lines[0].strip()
            term_expansion = None
            if term_name.find("|") >= 0:
                # This is an acronym with an expansion
                values = term_name.split("|")
                if len(values) > 2:
                    self.pp.error("Glossary term syntax is incorrect. Expected 'Term | Expansion' and got '%s'"%(term_name))
                    continue
                term_name = values[0].strip()
                term_expansion = values[1].strip()
            term_definition = "\n".join(lines[1:])
            self.terms[term_name] = Term(term_name, term_expansion, term_definition)
            new_terms[term_name] = self.terms[term_name]
        return new_terms
            
    def glossary2html(self):
        """
        Produce a table of all of the terms inserted with cross-reference links.
        """

        # Place the glossary table first
        tid = ' id="%s"'%self.pp.title2id("table-glossary")
        s = '<div class="table"%s><table>\n'%tid
        s += "<thead><tr>\n"
        header = ["Term", "Definition"]
        for d in header:
            s += "  <th>%s</th>\n" % d
        s += "</tr></thead>\n"

        for name in sorted(self.terms.keys()):
            term = self.terms[name]
            s += "<tr>\n"
            if (term.expansion == None):
                s += "  <td>%s</td><td><a id=\"glossary_%s\"/>%s</td>\n" % (term.name, term.name, term.description)
            else:
                # This term has an acronym expansion.
                s += "  <td>%s</td><td><a id=\"glossary_%s\"/><b>%s</b><br>%s</td>\n" % (term.name, term.name, term.expansion, term.description)
            s += "</tr>"
        s += "</table>\n"
        s += '<p class="table_caption">Glossary</p>\n'
        s += "</div>\n\n"

        return s

new = [GlossaryPlugin]
