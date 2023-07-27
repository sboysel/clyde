all: erogen/pcbs/clyde.kicad_pcb

erogen/pcbs/clyde.kicad_pcb: clyde.yaml
	npm run gen

clean:
	rm -rf ergogen 
