# greengraph
The first assignment for the Research Software Engineering with Python module at UCL. This Python package is used to uses Google Maps to plot “urbanisation” (green pixels intensity) between two specified locations. The program accepts four arguments: First location name, second location name, number of steps between locations and name of the output file.

##Installation
The package can be installed using pip:
```bash
pip install git+git://github.com/janzmazek/greengraph.git
```
or if you want a local copy of the repository
```bash
git clone https://github.com/janzmazek/greengraph.git
```
```bash
python setup.py install
```

##Usage
The package can be run using command line with command greengraph. To specify input arguments, use
-	--from (or –f): starting location,
-	--to (or –t): ending location,
-	--steps (or –s): number of steps between the locations,
-	--out or (–o): name of the output file.
Example:
```bash
greengraph --from “Ljubljana” --to “London” --steps 50 --out “plot.png” ```
