## Setup for the tutorial [](https://react.dev/learn/tutorial-tic-tac-toe#setup-for-the-tutorial "Link for Setup for the tutorial ")
In the live code editor below, click **Fork** in the top-right corner to open the editor in a new tab using the website CodeSandbox. CodeSandbox lets you write code in your browser and preview how your users will see the app you’ve created. The new tab should display an empty square and the starter code for this tutorial.
App.js
App.js
ReloadClear Fork
9
1
2
3
4
export default function Square() {
return <button className="square">X</button>;
}


You can also follow this tutorial using your local development environment. To do this, you need to:
  1. Install
  2. In the CodeSandbox tab you opened earlier, press the top-left corner button to open the menu, and then choose **Download Sandbox** in that menu to download an archive of the files locally
  3. Unzip the archive, then open a terminal and `cd` to the directory you unzipped
  4. Install the dependencies with `npm install`
  5. Run `npm start` to start a local server and follow the prompts to view the code running in a browser


If you get stuck, don’t let this stop you! Follow along online instead and try a local setup again later.
