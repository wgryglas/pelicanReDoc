

This is customized Pelican Docs template for generating 
documentation and tutorials based on RST files with 
custom roles, directives etc. All pluguable stuff for pelican (mostyl modification 
at docutils level, plus possible pelican toolset extensions) would be located 
under the plugins director. 

This is a development area. Currently we are basing on Pelican Docs which 
joins docutils with jinja templating. Pelican glues all the stuff to produce
certain static website. Perhaps in the future we will move back from Pelican if
it will be more convenient to develop own glue as Pelican in certain area might 
appear to be not flexible enough. However at this point Pelican should be used over
re-inventing the wheel  


To make it work you need to install additional python packages:
  - pip install --no-cache-dir --upgrade setuptools
  - pip install --no-cache-dir --upgrade docutils
  - pip install --no-cache-dir --upgrade pelican
  - pip install --no-cache-dir --upgrade loremipsum 
  - pip install --no-cache-dir --upgrade invoke

then you just go to the root dir and apply command:

> invoke build

and all sites would be placed under "./output" subdirectory. The "invoke" tool executes
commands stored in "tesks.py" script, therefore it is easy to configure it for making 
own publishing steps and etc. 

