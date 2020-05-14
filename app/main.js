const { app, BrowserWindow } = require('electron');
const createWindow = () => {
    const win = new BrowserWindow({
        width: 1440,
        height: 1080,
        webPreferences: {
            nodeIntegration: true
        }
    });
    win.loadFile('index.html');
    win.webContents.openDevTools()

};

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== "darwin") app.quit();
});

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow(); 
})