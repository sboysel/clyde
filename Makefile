all: choc/pcbs/clyde-choc.kicad_pcb mx/pcbs/clyde-mx.kicad_pcb

choc/pcbs/clyde-choc.kicad_pcb: choc/clyde-choc.yaml
	npm run choc

mx/pcbs/clyde-mx.kicad_pcb: mx/clyde-mx.yaml
	npm run mx

clean:
	rm -rf choc/pcbs/clyde-choc.kicad_pcb
	rm -rf mx/pcbs/clyde-mx.kicad_pcb
