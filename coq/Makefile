# Coq Makefile for I-Algebra

COQC = coqc
COQDEP = coqdep
COQFLAGS = -R . IAlgebra

VFILES = IAlgebra.v ExtendedAnalysis.v

all: $(VFILES:.v=.vo)

%.vo: %.v
	$(COQC) $(COQFLAGS) $<

depend:
	$(COQDEP) $(COQFLAGS) $(VFILES) > .depend

clean:
	rm -f *.vo *.glob *.aux .depend

.PHONY: all depend clean

-include .depend
