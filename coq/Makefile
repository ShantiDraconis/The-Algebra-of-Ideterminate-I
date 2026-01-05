# Coq Makefile for I-Algebra

COQC = coqc
COQDEP = coqdep
COQFLAGS = -R . IAlgebra

VFILES = IAlgebra.v ExtendedAnalysis.v
# Makefile for Coq formalization of The Algebra of Indeterminate I
#
# This Makefile should be generated from _CoqProject using:
#   coq_makefile -f _CoqProject -o Makefile
#
# For now, we provide a simple manual version.

.PHONY: all clean

COQC = coqc
COQDEP = coqdep
COQFLAGS = -R theories AlgebraI

VFILES = theories/Basic.v

all: $(VFILES:.v=.vo)

%.vo: %.v
	$(COQC) $(COQFLAGS) $<

depend:
	$(COQDEP) $(COQFLAGS) $(VFILES) > .depend

clean:
	rm -f *.vo *.glob *.aux .depend

.PHONY: all depend clean
clean:
	rm -f theories/*.vo theories/*.glob theories/.*.aux

depend:
	$(COQDEP) $(COQFLAGS) $(VFILES) > .depend

-include .depend
