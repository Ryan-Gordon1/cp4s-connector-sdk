![IBM Security](./assets/IBM_Security_lockup_pos_RGB.png)
# cp4s-connector-sdk
The Cloud Pak for Security (CP4S) SDK is a tool provided as a part of the integration ecosystem to streamline the creation of new Connectors for either the CAR or UDI services.

## Use Cases 

### Generating Connectors:
Cloud Pak for Security exposes connectors as a new mechanism or point of integration for the platform. Alongside SOAR Functions, Playbooks and QRadar Apps; the CAR framework compliments the integration framework and this connector SDK aims to simplify the developer experience of working with Connectors.

Code generation is a powerful tool in a new ecosystem not only for helping to cultivate best practices among the community but also to help decrease the time to response for our users working with these tools.
Customers have to work with many many tools and ideally want to learn as little as possible about another tool. 

For this reason we provided a best practice package someone can take and simply extend. We called this the [car-reference-connector](https://github.com/IBM/cp4s-car-reference-connector) and distributed it over github. The generated connector packages from this tool are based on the reference package and provide a way for a developer to streamline the bootstrapping process of getting a new connector working. 

## Installation 

### Get from pypi Pypi : 
The package is currently available on the test pypi in order to preserve the namespace for IBM on the main pypi repo
To install this from the test pypi :
```bash
pip install -i https://test.pypi.org/simple/ cp4s-connector-sdk==0.0.1
```


### Install locally
+ `git clone <url>`
+ `cd cp4s-connector-sdk`
+ `python setup.py install` 

The above will install the sdk but if you want to make changes to the SDK and see those changes on next run rather than needing to reinstall the package use the develop flag:
`python setup.py develop` 

## Usage 
### Available Commands 
#### `codegen:`
Generate boilerplate code to start developing a connector
```
connector-sdk codegen -p my_aws_connector
```
Coming soon -- generate boilerplates for any of the connectors 
```
connector-sdk codegen -p my_udi_connector --connectortype UDI
```