all:
	python main.py -p python main.py -p sample/sample_2.jpg -sr 6
clean:	
	rm -fr ./out 
	mkdir ./out
install:
	pip install opencv-contrib-python