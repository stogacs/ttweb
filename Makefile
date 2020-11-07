TARGET ?= target

LATEXMK ?= latexmk

DOCKER ?= docker

.PHONY : index index-docker create-target

index : create-target index.tex $(wildcard sections/*) references.bib
	$(LATEXMK)

index-docker : create-target index.tex $(wildcard sections/*) references.bib
	DOCKER_BUILDKIT=1	$(DOCKER) build --output $(TARGET) .

create-target :
	@mkdir -p $(TARGET)
