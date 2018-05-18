Kopernikus
==========

A tool to check multile Domains if they are up and running.

## Commands <sup><small>and what they internally do</small></sup>

### install
- create local database
- add local IP to satellites
- set log number to 0
- create query domain 1min cron
- create query satellite 15 min cron

### connect *IP*
- add IP as satellite 
- ask satellite for more satellites
- add additional satellites
- add domains from satellite to query db
- set lognumber to the one from satellite

### add *DOMAIN*
- add *DOMAIN* to query database
  - check if valid domain
- inform satellites about new domain
- increase satellite log number

### del *DOMAIN*
- remove *DOMAIN* from query database
- inform satellites about removed domain
- increase satellite log number

### query domain
- cycle through query database and checks domain
- check domain
  - 200 OK
  - any other bad
  - log result

### query satellite
- get domain query log from satellite
- ask for log number
  - if other higher
    - update domain list from satellite
    - update satellite list from satellite

### result
- list domains reachablity(idk if this is a word but you now ..) in %
- if 33% of satellites cant

### clean result keep *DAYS*
- remove every entry from domain query log older than *DAYS*

### clean all
- remove database