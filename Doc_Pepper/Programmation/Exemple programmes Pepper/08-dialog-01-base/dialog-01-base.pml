<?xml version="1.0" encoding="UTF-8" ?>
<Package name="dialog-01-base" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="blabla" src="blabla/blabla.dlg" />
        <Dialog name="ExampleDialog" src="behavior_1/ExampleDialog/ExampleDialog.dlg" />
    </Dialogs>
    <Resources>
        <File name="" src=".metadata" />
        <File name="translation_en_US" src="translations/translation_en_US.ts" />
    </Resources>
    <Topics>
        <Topic name="blabla_frf" src="blabla/blabla_frf.top" topicName="blabla" language="fr_FR" />
        <Topic name="ExampleDialog_enu" src="behavior_1/ExampleDialog/ExampleDialog_enu.top" topicName="ExampleDialog" language="en_US" />
    </Topics>
    <IgnoredPaths>
        <Path src=".metadata" />
    </IgnoredPaths>
</Package>
