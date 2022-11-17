<?xml version="1.0" encoding="UTF-8" ?>
<Package name="basique" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="behaviour2" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="gr" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="fsdf" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="gggggfdbd" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="testdial" src="testdial/testdial.dlg" />
    </Dialogs>
    <Resources>
        <File name="translations" src="behavior_1/translations.csv" />
    </Resources>
    <Topics>
        <Topic name="testdial_enu" src="testdial/testdial_enu.top" topicName="testdial" language="en_US" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
