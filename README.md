# FLOPX

## Overview

FLOPX allows the client to execute computational tasks on behalf of the host for tokens which can be exchanged for services and digital goods provided by the host. This project provides a potential alternative to advertisement based monetization models for digital content. This project is under development and is currently a prototype.

## Getting Started

### Prerequisites
This project requires Python 3 and Flask. Installing the latest [Anaconda for Python 3.x](https://www.anaconda.com/distribution/#download-section) should give you everything you need to hit the ground running.

### Setup
Clone the project and enter the resulting directory:

    $ git clone git@github.com:jonathanmann/flopx.git 
    $ cd flopx/

Make the start_server.sh script executable:

    $ chmod +x start_server.sh

Start the server:

    $ ./start_server.sh

Use your browser to connect to the default server as displayed your console (probably [http://127.0.0.1:5000/](http://127.0.0.1:5000)).

### Usage
Use your favorite editor to update the script_inject.js file to have whatever javascript code you need executed on the client's system. By default, when the script completes the results are passed to the '/verify' route via POST. 

Similarly, update the content.html file to provide the content your clients are performing compute tasks to get.

Add your own audits and verification methods to prevent clients from cheating.

## Roadmap
>> add persona identifiers
>> validation hashes for proof of work
>> token accounting
>> remote instruction inputs
>> sandboxed compute tasks
>> token persistence
