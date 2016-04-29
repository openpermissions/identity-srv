FORMAT: 1A
HOST: https://id-stage.copyrighthub.org

# Open Permissions Platform Identity Service
The Identity Service is required to create unique Ids for
* Asset
* Offer
* Agreement

## Standard error output
On endpoint failure there is a standard way to report errors.
The output should be of the form

| Property | Description               | Type   |
| :------- | :----------               | :---   |
| status   | The status of the request | number |
| errors   | A list of errors          | list   |

### Error
| Property | Description                                 | Type   |
| :------- | :----------                                 | :---   |
| source   | The name of the service producing the error | number |
| message  | A description of the error                  | string |

# Authorization

This API requires authentication. Where [TOKEN] is indicated in an endpoint header you should supply an OAuth 2.0 access token with the appropriate scope (read, write or delegate). 

See [How to Auth](https://github.com/openpermissions/auth-srv/blob/master/documents/markdown/how-to-auth.md) 
for details of how to authenticate Hub services.

# Group Identity

## Identity service information [/v1/identity]

### Retrieve service information [GET]

#### Output
| Property | Description               | Type   |
| :------- | :----------               | :---   |
| status   | The status of the request | number |
| data     | The service information   | object |

##### Service information
| Property     | Description                    | Type   |
| :-------     | :----------                    | :---   |
| service_name | The name of the api service    | string |
| service_id   | The id of the api service      | string |
| version      | The version of the api service | string |


+ Request service information
    + Headers

            Accept: application/json

+ Response 200 (application/json; charset=UTF-8)
    + Body

            {
                "status": 200,
                "data": {
                    "service_name": "Open Permissions Platform Identity Service",
                    "service_id": "8460433ee21111e597309a79f06e9478",
                    "version": "0.8.0"
                }
            }


# Group Capabilities

## Identity service capabilities [/v1/identity/capabilities]

### Retrieve service information [GET]

| OAuth Token Scope |
| :----------       |
| read              |

#### Output
| Property | Description               | Type   |
| :------- | :----------               | :---   |
| status   | The status of the request | number |
| data     | The service capabilities  | object |

##### Service capabilities
| Property                | Description                                                         | Type   |
| :-------                | :----------                                                         | :---   |
| max_id_generation_count | The maximum number of ids that can be created in a single operation | number |


+ Request service capabilities
    + Headers

            Accept: application/json
            Authorization: Bearer [TOKEN]

+ Response 200 (application/json; charset=UTF-8)
    + Body

            {
                "status": 200,
                "data": {
                    "max_id_generation_count": 1024
                }
            }

# Group Asset

## Identity generation for asset [/v1/identity/asset]

### Create asset identities [POST]

| OAuth Token Scope |
| :----------       |
| write             |

#### Input
| Property      | Description                                                                              | Type   | Mandatory |
| :-------      | :----------                                                                              | :---   | :-------  |
| resolver_id   | The name of the host that can resolve the hub key. Must be a valid hostname and protocol | string | yes       |
| hub_id        | The id of the hub that is hosting the key                                                | string | yes       |
| repository_id | ID of the repository that contains the entity                                            | string | yes       |
| count         | Number of asset ids to create. Must be greater than 0. (Default: 1)                      | number | no        |

#### Output
| Property | Description               | Type   |
| :------- | :----------               | :---   |
| status   | The status of the request | number |
| data     | List of asset uids        | list   |


+ Request Create one or more asset ids (application/json)
    
    + Headers

            Accept: application/json
            Authorization: Bearer [TOKEN]
            
    + Body

            {
                "resolver_id": "https://copyrighthub.org",
                "hub_id": "hub1",
                "repository_id": "10e4b9612337f237118e1678ec001fa6",
                "count": 3
            }


+ Response 200 (application/json; charset=UTF-8)

    + Body

            {
                "status": 200,
                "data": [
                    "https://copyrighthub.org/s1/hub1/10e4b9612337f237118e1678ec001fa6/asset/5d84d36d6eec446aae9c4435291eca8a",
                    "https://copyrighthub.org/s1/hub1/10e4b9612337f237118e1678ec001fa6/asset/749ac740da53480d81f8568240e93fb2",
                    "https://copyrighthub.org/s1/hub1/10e4b9612337f237118e1678ec001fa6/asset/d9a6b7fe4c0f4343945b13eb8e78fb74"
                ]
            }

+ Request Create asset ids with invalid data (application/json)
    
    + Headers

            Accept: application/json
            Authorization: Bearer [TOKEN]
            
    + Body

            {
               "resolver_id": "not a URL",
               "repository_id": "not a uuid",
               "count": 2000,
               "unknown": "x"
             }

+ Response 400 (application/json; charset=UTF-8)

    + Body

            {
                "status": 400,
                "errors": [
                    {
                        "message": "Field 'count' value must be at most 1024",
                        "source": "identity"
                    },
                    {
                        "message": "Field 'repository_id' does not match regular expression '[0-9a-f]{32}'",
                        "source": "identity"
                    },
                    {
                        "message": "Field 'resolver_id' does not match regular expression 'https://(?:[a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])(?:\\.(?:[a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9]))*(?::[0-9]{2,5})?'",
                        "source": "identity"
                    },
                    {
                        "message": "Unexpected field 'unknown'",
                        "source": "identity"
                    }
                ]
            }

+ Request Create asset ids with empty data (application/json)

    + Headers

            Accept: application/json
            Authorization: Bearer [TOKEN]
            
    + Body

            {}

+ Response 400 (application/json; charset=UTF-8)

    + Body

            {
                "status": 400,
                "errors": [
                    {
                        "message": "Missing 'hub_id'",
                        "source": "identity"
                    },
                    {
                        "message": "Missing 'repository_id'",
                        "source": "identity"
                    },
                    {
                        "message": "Missing 'resolver_id'",
                        "source": "identity"
                    }
                ]
            }


# Group Offer

## Identity generation for offer [/v1/identity/offer]

### Create offer identities [POST]

| OAuth Token Scope |
| :----------       |
| write             |

#### Input
| Property      | Description                                                                              | Type   | Mandatory |
| :-------      | :----------                                                                              | :---   | :-------  |
| resolver_id   | The name of the host that can resolve the hub key. Must be a valid hostname and protocol | string | yes       |
| hub_id        | The id of the hub that is hosting the key                                                | string | yes       |
| repository_id | ID of the repository that contains the entity                                            | string | yes       |
| count         | Number of asset ids to create. Must be greater than 0. (Default: 1)                      | number | no        |

#### Output
| Property | Description               | Type   |
| :------- | :----------               | :---   |
| status   | The status of the request | number |
| data     | List of offer uids        | list   |


+ Request Create one or more offer ids (application/json)
    
    + Headers

            Accept: application/json
            Authorization: Bearer [TOKEN]
                
    + Body

            {
                "resolver_id": "https://copyrighthub.org",
                "hub_id": "hub1",
                "repository_id": "10e4b9612337f237118e1678ec001fa6",
                "count": 3
            }


+ Response 200 (application/json; charset=UTF-8)

    + Body

            {
                "status": 200,
                "data": [
                    "https://copyrighthub.org/s1/hub1/10e4b9612337f237118e1678ec001fa6/offer/5d84d36d6eec446aae9c4435291eca8a",
                    "https://copyrighthub.org/s1/hub1/10e4b9612337f237118e1678ec001fa6/offer/749ac740da53480d81f8568240e93fb2",
                    "https://copyrighthub.org/s1/hub1/10e4b9612337f237118e1678ec001fa6/offer/d9a6b7fe4c0f4343945b13eb8e78fb74"
                ]
            }


+ Request Create offer ids with invalid data (application/json)

    + Headers

            Accept: application/json
            Authorization: Bearer [TOKEN]
                
    + Body

            {
               "resolver_id": "not a URL",
               "repository_id": "not a uuid",
               "count": 2000,
               "unknown": "x"
             }

+ Response 400 (application/json; charset=UTF-8)

    + Body

            {
                "status": 400,
                "errors": [
                    {
                        "message": "Field 'count' value must be at most 1024",
                        "source": "identity"
                    },
                    {
                        "message": "Field 'repository_id' does not match regular expression '[0-9a-f]{32}'",
                        "source": "identity"
                    },
                    {
                        "message": "Field 'resolver_id' does not match regular expression 'https://(?:[a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])(?:\\.(?:[a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9]))*(?::[0-9]{2,5})?'",
                        "source": "identity"
                    },
                    {
                        "message": "Unexpected field 'unknown'",
                        "source": "identity"
                    }
                ]
            }

+ Request Create offer ids with empty data (application/json)

    + Headers

            Accept: application/json
            Authorization: Bearer [TOKEN]
                
    + Body

            {}
            


+ Response 400 (application/json; charset=UTF-8)

    + Body

            {
                "status": 400,
                "errors": [
                    {
                        "message": "Missing 'hub_id'",
                        "source": "identity"
                    },
                    {
                        "message": "Missing 'repository_id'",
                        "source": "identity"
                    },
                    {
                        "message": "Missing 'resolver_id'",
                        "source": "identity"
                    }
                ]
            }


# Group Agreement

## Identity generation for agreement [/v1/identity/agreement]

### Create agreement identities [POST]

| OAuth Token Scope |
| :----------       |
| write             |

#### Input
| Property      | Description                                                                              | Type   | Mandatory |
| :-------      | :----------                                                                              | :---   | :-------  |
| resolver_id   | The name of the host that can resolve the hub key. Must be a valid hostname and protocol | string | yes       |
| hub_id        | The id of the hub that is hosting the key                                                | string | yes       |
| repository_id | ID of the repository that contains the entity                                            | string | yes       |
| count         | Number of asset ids to create. Must be greater than 0. (Default: 1)                      | number | no        |

#### Output
| Property | Description               | Type   |
| :------- | :----------               | :---   |
| status   | The status of the request | number |
| data     | List of agreement uids    | list   |


+ Request Create one or more agreement ids (application/json)
    
    + Headers

            Accept: application/json
            Authorization: Bearer [TOKEN]
                
    + Body

            {
                "resolver_id": "https://copyrighthub.org",
                "hub_id": "hub1",
                "repository_id": "10e4b9612337f237118e1678ec001fa6",
                "count": 3
            }


+ Response 200 (application/json; charset=UTF-8)

    + Body

            {
                "status": 200,
                "data": [
                    "https://copyrighthub.org/s1/hub1/10e4b9612337f237118e1678ec001fa6/agreement/5d84d36d6eec446aae9c4435291eca8a",
                    "https://copyrighthub.org/s1/hub1/10e4b9612337f237118e1678ec001fa6/agreement/749ac740da53480d81f8568240e93fb2",
                    "https://copyrighthub.org/s1/hub1/10e4b9612337f237118e1678ec001fa6/agreement/d9a6b7fe4c0f4343945b13eb8e78fb74"
                ]
            }


+ Request Create agreement ids with invalid data (application/json)

    + Headers

            Accept: application/json
            Authorization: Bearer [TOKEN]
                
    + Body

            {
               "resolver_id": "not a URL",
               "repository_id": "not a uuid",
               "count": 2000,
               "unknown": "x"
             }

+ Response 400 (application/json; charset=UTF-8)

    + Body

            {
                "status": 400,
                "errors": [
                    {
                        "message": "Field 'count' value must be at most 1024",
                        "source": "identity"
                    },
                    {
                        "message": "Field 'repository_id' does not match regular expression '[0-9a-f]{32}'",
                        "source": "identity"
                    },
                    {
                        "message": "Field 'resolver_id' does not match regular expression 'https://(?:[a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])(?:\\.(?:[a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9]))*(?::[0-9]{2,5})?'",
                        "source": "identity"
                    },
                    {
                        "message": "Unexpected field 'unknown'",
                        "source": "identity"
                    }
                ]
            }

+ Request Create agreement ids with empty data (application/json)

    + Headers

            Accept: application/json
            Authorization: Bearer [TOKEN]
                
    + Body

            {}


+ Response 400 (application/json; charset=UTF-8)

    + Body

            {
                "status": 400,
                "errors": [
                    {
                        "message": "Missing 'hub_id'",
                        "source": "identity"
                    },
                    {
                        "message": "Missing 'repository_id'",
                        "source": "identity"
                    },
                    {
                        "message": "Missing 'resolver_id'",
                        "source": "identity"
                    }
                ]
            }
