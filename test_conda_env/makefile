

install: # create your virtual environment
	@echo "Creating virtual environment"
	conda create --prefix ./my_temp_conda_env python=3.8.3 --file=package-list.txt

plot: # generate interactive plot
	echo "generating interactive plot (.html file)"
	./my_temp_conda_env/bin/python HCP_interactive_plot.py

clean: # delete your virtual environment
	@echo "Cleaning up"
	rm -rf ./my_temp_conda_env
