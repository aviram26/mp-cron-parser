## Publish to PyPi

* Make relevant changes
* Update pyproject.toml `version` field
* Push anf verify build job is green
* Create new tag

```git
# align tag with version
git tag <my-new-tag> 
git push origin <my-new-tag>
```

This will trigger the action correctly and update PyPi version
