#
# Makefile to generate xhtml, pdf formats from asciidoc sources
#
# Author: Francesco Minafra <Francesco.Minafra@clustervision.com>
# Suggestions came from
# https://groups.google.com/forum/#!searchin/asciidoc/makefile
# https://groups.google.com/d/msg/asciidoc/4YMJY2-SvIw/augMMjhb0WcJ
# https://github.com/tschaume/wp-pdf
#

DOCOUT = index

# We first build the lists of targets:
#
# Search for all the asciidoc source files (of the form *.txt)
# both in the current directory and its subdirectories
HTML = $(patsubst %.txt,%.html,$(shell find -name \*.txt))
PDF = $(patsubst %.txt,%.pdf,$(shell find -name \*.txt))
TXT = $(shell find -name \*.txt)
# 
# files docinfo.xml and $(DOCOUT)-docinfo.xml are also targets
DOCINFO = $(shell find -name \*docinfo.xml)

# define the A2X command:
#
# arguments: $(1) format (pdf/html), $(2) asciidoc file
# -a docinfo = include $(DOCOUT)-docinfo.xml


define A2XCMD
a2x -vv -a docinfo -a icons --dblatex-opts "-P latex.output.revhistory=0 -P doc.publisher.show=0" -L -f $(1) $(2)
#a2x -vv -a docinfo -a icons --fop --dblatex-opts "-P latex.output.revhistory=0 -P doc.publisher.show=0" -L -f $(1) $(2)
endef

# Default target if none specified
all: html

html: $(HTML) 
	$(shell ./mktag.sh)
pdf: $(PDF)

# $(<D) : Directory part of the first prerequisite
# $(<F) : File-within-directory part of the first prerequisite
#

# Generate XHTML
# For large documents that include sub-documents, the root document 
# tends to not be recompiled if any of the 
# included parts are changed.
$(DOCOUT).html: $(TXT)
# The following rule uses the shared CSS for xhtml11 and html5 backends
%.html: %.txt $(DOCINFO)
	cd $(<D) && asciidoc -v -a icons -a data-uri -a toc2 -a max-width=55em $(<F)
#	cd $(<D) && a2x -vv -a docinfo -a icons -a data-uri -a toc2 -a max-width=55em -f xhtml $(<F)
#	cd $(<D) && $(call A2XCMD,xhtml,$(<F))

# Generate pdf
%.pdf: %.txt
	cd $(<D) && $(call A2XCMD,pdf,$(<F))

# Phony targets are declared explicitly, in case there is e.g. some file called 'all' or 'clean'
# that interferes with make operations.
# Phony takes target always as out-of-date
.PHONY: all html pdf clean

# Clean up rule 
clean:
	@for f in $(HTML) $(PDF) messages; do if [ -f $$f ]; then rm "$$f"; echo "rm $$f"; fi; done
