SOURCES = lilypond-four-weeks.tely

out/html/index.html: temp/lilypond-four-weeks/index.html
	mkdir -p out/html/
	cp -a temp/lilypond-four-weeks/. out/html/
	cd temp; find . -regex ".*/[0-9a-f][0-9a-f]/lily-.*\.png" -type f -exec rsync -R {} ../out/html \;
	cd temp; find . -regex ".*/[0-9a-f][0-9a-f]/lily-.*\.ly" -type f -exec rsync -R {} ../out/html \;

temp/lilypond-four-weeks/index.html: temp/lilypond-four-weeks.texi
	cd temp; texi2any --html lilypond-four-weeks.texi

out/html/lilypond-four-weeks-large.html: temp/lilypond-four-weeks.html
	mkdir -p out/html/
	cp temp/lilypond-four-weeks.html out/html/lilypond-four-weeks-large.html

temp/lilypond-four-weeks.html: temp/lilypond-four-weeks.texi
	cd temp; texi2any --html --no-split lilypond-four-weeks.texi

out/pdf/lilypond-four-weeks.pdf: temp/lilypond-four-weeks.pdf
	mkdir -p out/pdf/
	cp temp/lilypond-four-weeks.pdf out/pdf/

temp/lilypond-four-weeks.pdf: temp/lilypond-four-weeks.texi
	cd temp; PDFTEX=xetex texi2any --pdf -I ../tex/ lilypond-four-weeks.texi

temp/lilypond-four-weeks.texi: ${SOURCES}
	lilypond-book --pdf -o temp/ lilypond-four-weeks.tely

pdf: out/pdf/lilypond-four-weeks.pdf
html: out/html/index.html
html-large: out/html/lilypond-four-weeks-large.html

all: pdf html html-large

clean:
	rm -r temp/
	rm -r out/
