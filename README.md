# hp-disk-status-getter
A utility for collecting metrics about the status of hard drives from HP servers of generation 10 and higher.
## Desciption
This utility is designed to collect metrics about the status of hard drives from HP raid controllers using the ssacli utility supplied by HP and then output metrics in the openmetrics format. For this utility to work properly, a package with ssacli utilities must be installed on the server (see here: https://support.hpe.com/connect/s/softwaredetails?collectionId=MTX-51c52bf006bd4c60) also python3.

## Install & run

```
# under root user
cd /opt/ && git clone https://github.com/constantinekg/hp-disk-status-getter && cd hp-disk-status-getter
```

After this you can run and return output into file like this:

```
/opt/hp-disk-status-getter/get.py > somewhere.prom
```
