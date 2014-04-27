Requirements:
    Generic:
        yac_scrypt
        Python
        Twisted
        python-argparse (for Python <=2.6)
    
    Linux:
        sudo apt-get install python-zope.interface python-twisted python-twisted-web
        sudo apt-get install python-argparse # if on Python 2.6 or older
    
    Windows:
        Install Python 2.7: http://www.python.org/getit/
        Install Twisted: http://twistedmatrix.com/trac/wiki/Downloads
        Install Zope.Interface: http://pypi.python.org/pypi/zope.interface/3.8.0
            Unzip the files into C:\Python27\Lib\site-packages

Additional info about scrypt module:
        In order to run P2Pool with the EcoCoin network, you would need to build and install the
        ltc_scrypt module that includes the scrypt proof of work code that EcoCoin uses for block hashes.

        Linux:
            cd yac_scrypt
            sudo python setup.py install

        Windows:
            Install MinGW: http://www.mingw.org/wiki/Getting_Started
            Install Python 2.7: http://www.python.org/getit/

            cd litecoin_scrypt
            C:\Python27\python.exe setup.py build --compile=mingw32 install

            If you run into an error with unrecognized command line option '-mno-cygwin', see this:
                http://stackoverflow.com/q/6034390/1260906

Running P2Pool:
    To use P2Pool, you must be running your own local ecocoind. For standard
    configurations, using P2Pool should be as simple as:

        python run_p2pool.py

    Then run your miner program, connecting to 127.0.0.1 on port 22337 with any
    username and password.

    If you are behind a NAT, you should enable TCP port forwarding on your
    router. Forward port 9777 to the host running P2Pool.

    Run "python run_p2pool.py --help" for additional options.