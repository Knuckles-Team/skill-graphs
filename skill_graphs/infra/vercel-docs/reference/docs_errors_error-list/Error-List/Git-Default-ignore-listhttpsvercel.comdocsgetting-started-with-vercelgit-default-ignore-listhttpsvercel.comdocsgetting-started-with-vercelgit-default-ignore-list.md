##  [Git Default ignore list](https://vercel.com/docs/getting-started-with-vercel#git-default-ignore-list)[](https://vercel.com/docs/getting-started-with-vercel#git-default-ignore-list)
Deployments created using Vercel CLI will automatically [ignore several files](https://vercel.com/docs/deployments/build-features#ignored-files-and-folders) for security and performance reasons.
However, these files are _not_ ignored for deployments created using [Git](https://vercel.com/docs/git) and a warning is printed instead. This is because `.gitignore` determines which files should be ignored.
If the file was intentionally committed to Git, you can ignore the warning.
If the file was accidentally committed to Git, you can remove it using the following commands:
terminal
```
git rm file.txt                   # remove the file
echo 'file.txt' >> .gitignore     # append file to .gitignore
git add .gitignore                # stage the change
git commit -m "Removed file.txt"  # commit the change
git push                          # deploy the change
```
