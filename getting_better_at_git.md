# Git

## Create a repo from CLI

```bash
curl -v \
-X POST \
 -H "Accept: application/vnd.github.v3+json" \
 https://api.github.com/user/repos \
 -d '{"name":"advent_of_code_2020","private":"true"}' \
 -u sciarrilli
```

_Input API Key at prompt_

## In local directory

1. Init the directory for git.

```bash
git init
```

2. Add the remote origin.

```bash
git remote add origin git@github.com:sciarrilli/advent_of_code_2020.git
```

3. Add all local files

```bash
git add .
```

4. Commit the updates

```bash
git commit -m 'init'
```

5. Upload the files to the remote repo

```bash
git push -u origin master
```
