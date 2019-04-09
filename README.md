## Scarlet Exporter

This is a simple Python utility to export notes from an Android
note-taking app, [Scarlet Notes][ScarletPlayStore]. It currently only
supports a single output format, the one used by Notable.

I liked Scarlet Notes a lot till the recent update, which radically changed the interface, replacing the good old monospaced fonts with
sans serif and adding lots of popups and suggestions I didn't like. So
I wrote this little tool to export all of my notes to Notable.

#### Usage

First export your notes from Scarlet in the plain text format. Then run:

    % python -m scarlet_export -o OUTPUTDIR exported_file.txt

#### License

See [this file](LICENSE).

[ScarletPlayStore]: https://play.google.com/store/apps/details?id=com.bijoysingh.quicknote "Link to Google Play Store"
