# Obtain the otxecm Helm Chart
To add the OpenText Helm repository to Helm’s list of repositories:    
```helm repo add opentext https://registry.opentext.com/helm --username <user@example.com> --password <Password>```

Refresh your Helm repository information by running:  
```helm repo update.```

Obtain the version of the otxecm Helm chart that you require by running:  
```helm pull opentext/otxecm --version=<##.#.#>```

To extract the Helm chart into your current directory add the --untar command argument:
```helm pull opentext/otxecm --version=<##.#.#> --untar```

The helm install command is used to install a Helm chart:    
```helm install [RELEASE_NAME] [CHART] [flags]```

To install helm chart existing in current directory:  
```helm install release-name .```

The helm list command lists all the releases:  
```helm list```  

The helm delete command deletes a release.  
``` helm delete [RELEASE_NAME] [flags]```
