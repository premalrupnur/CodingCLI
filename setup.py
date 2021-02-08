from setuptools import setup, find_packages 

with open('requirements.txt') as f: 
	requirements = f.readlines() 

long_description = 'This is a command line tool that helps you track your daily coding activities,using wakatime API '

setup( 
		name ='CodingMetrics', 
		version ='1.0.0', 
		author ='Premal Rupnur', 
		author_email ='premalrupnur2001@gmail.com', 
		url ='https://github.com/premalrupnur/CodingCLI', 
		description ='Your coding activity tracker', 
		long_description = long_description, 
		long_description_content_type ="text/markdown", 
		license ='MIT', 
		include_package_data=True,
		packages = find_packages(), 
        entry_points ={ 
            'console_scripts': [ 
                'coding-cli = commands.main:main'
            ] 
        }, 
		classifiers =[
			"Programming Language :: Python :: 3", 
			"License :: OSI Approved :: MIT License", 
			"Operating System :: OS Independent", 
        ], 
		install_requires = requirements, 
		zip_safe = False,

) 
