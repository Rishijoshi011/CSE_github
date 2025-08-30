import express from 'express';
import fs from 'fs';
import path from 'path';

const app = express();
const port = 3000;

app.get('/', (req, res) => {
    res.send('Hello World!');
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});

const dir = './random_files';

if (!fs.existsSync(dir)) {
    console.log('Directory not found');
} else {
    fs.readdirSync(dir, { withFileTypes: true }).forEach(dirent => {
        if (dirent.isFile()) {
            const fileName = dirent.name;
            const extension = fileName.split('.').pop();
            const extensionFolder = path.join(dir, extension);

            if (!fs.existsSync(extensionFolder)) {
                fs.mkdirSync(extensionFolder);
            }

            const oldPath = path.join(dir, fileName);
            const newPath = path.join(extensionFolder, fileName);

            fs.renameSync(oldPath, newPath);

            console.log(`Moved ${fileName} to folder ${extension}`);
        }
    });
}
