from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, HiddenField
from wtforms.validators import AnyOf, Length, DataRequired
from app.validators import MultiCheckboxField, AtLeastOneChecked, AtMostOneChecked, AlphaSpace, ValidZipCode, AlphaSpaceHyphen


class PhobForm(FlaskForm):

    formType = HiddenField("formType", default='Phob',
                           validators=[DataRequired(), AnyOf(['Phob'])])

    phobWarningX = RadioField(validators=[DataRequired()], choices=[
        ('I understand', 'I understand the risks associated with using a Phob on the Nintendo Switch')])

    handle = StringField(validators=[DataRequired(), Length(max=38)])

    useCase = RadioField(validators=[DataRequired()], choices=[
        ('Ultimate', 'Ultimate'), ('Melee', 'Melee'), ('Both', 'Both')])

    frontShell = StringField(
        validators=[DataRequired(), Length(max=20), AlphaSpace()])

    frontShellQual = RadioField(validators=[DataRequired()], choices=[
        ('Low', 'Low'), ('Mid', 'Mid'), ('High', 'High'), ('Very High', 'Very High')])

    backShell = StringField(
        validators=[DataRequired(), Length(max=20), AlphaSpace()])

    backShellQual = RadioField(validators=[DataRequired()], choices=[
        ('Low', 'Low'), ('Mid', 'Mid'), ('High', 'High'), ('Very High', 'Very High')])

    motherboard = RadioField(validators=[DataRequired()], choices=[(
        'Phob', 'Phob ($150)')])

    grayStickbox = RadioField(validators=[DataRequired()], choices=[
        ('Factory New', 'Factory New ($15)'), ('A Tier', 'A Tier ($11)'), ('B Tier', 'B Tier ($2)')])

    cStickbox = RadioField(validators=[DataRequired()], choices=[
        ('Factory New', 'Factory New ($15)'), ('A Tier', 'A Tier ($11)'), ('B Tier', 'B Tier ($2)')])

    grayStickCap = RadioField(validators=[DataRequired()], choices=[
        ('Factory New', 'Factory New ($12)'), ('A Tier', 'A Tier ($7)'), ('B Tier', 'B Tier ($4)'), ('F Tier', 'F Tier (VERY WORN, FREE)')])

    cStickCap = RadioField(validators=[DataRequired()], choices=[
        ('Factory New', 'Factory New ($6)'), ('A Tier', 'A Tier ($3)'), ('B Tier', 'B Tier (FREE)')])

    upgrades = MultiCheckboxField(validators=[AtLeastOneChecked()], choices=[
        ('fnT3Bundle', 'Factory New T3 Bundle ($25, includes everything listed below)'), ('fnLowFricTrigPotent', 'Factory New Low Friction Trigger Potentiometers ($10)'), ('fnT3BtnTrigPads', 'Factory New T3 Button/Trigger Pads ($10)'), ('fnT3BtnTrigPieces', 'Factory New T3 Button/Trigger Pieces ($5)'), ('upgradeNone', 'None')])

    trigPotent = RadioField(validators=[DataRequired()], choices=[
        ('Factory New Low Friction', 'Factory New Low Friction ($10, does not double charge if selected above)'), ('Used', 'Used (FREE)')])

    btnTrigStickColor = RadioField(validators=[DataRequired()], choices=[
        ('Standard Gray', 'Standard Gray (FREE)'), ('Black Dyed OEM', 'Black Dyed OEM ($15, excludes sticks)'), ('Light Gray', 'Light Gray ($25, FREE with white shell combo)')])

    cord = RadioField(validators=[DataRequired()], choices=[
        ('Standard Black 2 Meter', 'Standard Black 2 Meter (FREE)'), ('Standard Black 3 Meter', 'Standard Black 3 Meter ($4)'), ('White 3 Meter', 'White 3 Meter ($30, FREE with white shell combo)'), ('Paracord 2 Meter', 'Paracord 2 Meter ($35, any color of your choosing)'), ('Paracord 3 Meter', 'Paracord 3 Meter ($45, any color of your choosing)')])

    notches = RadioField(validators=[DataRequired()], choices=[
        ('Wavedash', 'Wavedash ($24)'), ('Firefox', 'Firefox ($96, includes wavedash)'), ('None', 'None (shield drop notches come for free automatically)')])

    buttonMods = MultiCheckboxField(validators=[AtLeastOneChecked()], choices=[
        ('baldBtns', 'Bald Buttons ($70, not compatible with Black Dyed OEM and Mouse Click ABXY)'), ('mouseClickABXY', 'Mouse Click ABXY ($70, includes stabilized buttons for free, not compatible with bald buttons)'), ('stabilizedBtns', 'Stabilized Buttons ($4)'), ('zRemapX', 'Z Jump Remap Toggleable with X (FREE, pick one for me to swap, you can swap anytime)'), ('zRemapY', 'Z Jump Remap Toggleable with Y (FREE, pick one for me to swap, you can swap anytime)'), ('oemZ', 'OEM Z Button (FREE)'), ('tactileZ', 'Tactile Z (FREE)'), ('btnNone', 'None')])

    mouseClickTrig = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    shortPlug = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    longPlug = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    digTrigUltimate = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    stabilizedTrigs = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    shortenedSpring = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    removedSpring = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    rumbleMod = RadioField(validators=[DataRequired()], choices=[
        ('Regular', 'Regular (no modification, FREE)'), ('Disconnected Motor', "Disconnected Motor (motor weight remains but won't rumble, FREE)"), ('Removed Motor', 'Removed Motor (completely removes motor from shell, FREE)')])

    cordPlugColor = RadioField(validators=[DataRequired()], choices=[
        ('Default', 'Default (FREE)'), ('Indigo', 'Indigo ($5)'), ('Black', 'Black ($5)'), ('Orange', 'Orange ($5)'), ('Platinum', 'Platinum ($5)'), ('White', 'White ($25)'), ('Emerald', 'Emerald ($27)'), ('Luigi', 'Luigi ($30)'), ('Mario', 'Mario ($32)'), ('Club Nintendo', 'Club Nintendo ($30)'), ('Clear', 'Clear ($35)'), ('Panasonic', 'Panasonic ($50)'), ('Wario', 'Wario ($60)')])

    queueSkip = RadioField(validators=[DataRequired()], choices=[
        ('7 days', 'Ship within 7 days ($100)'), ('21 Days', 'Ship within 21 days ($50)'), ('49 Days', 'Ship within 49 days (FREE)')])

    firstLastName = StringField(validators=[DataRequired(), Length(max=30)])
    streetAddress = StringField(validators=[DataRequired(), Length(max=45)])
    city = StringField(
        validators=[DataRequired(), Length(max=20), AlphaSpaceHyphen()])
    state = StringField(
        validators=[DataRequired(), Length(max=20), AlphaSpace()])
    zipCode = StringField(
        validators=[DataRequired(), Length(max=15), ValidZipCode()])
    country = StringField(
        validators=[DataRequired(), Length(max=20), AlphaSpace()])

    readPriceGuide = RadioField(validators=[DataRequired()], choices=[(
        'I understand', 'Yes, I understand')])

    insurancePolicy = RadioField(validators=[DataRequired()], choices=[(
        'I understand', 'I have read the insurance policy and understand what is covered and what is not')])

    dmGio = RadioField(validators=[DataRequired()], choices=[(
        "DM'd", "Yes, I have DM'd, ready to submit!")])

    submit = SubmitField("Submit")


class OEMForm(FlaskForm):

    formType = HiddenField("formType", default='OEM',
                           validators=[DataRequired(), AnyOf(['OEM'])])

    handle = StringField(validators=[DataRequired(), Length(max=38)])

    useCase = RadioField(validators=[DataRequired()], choices=[
        ('Ultimate', 'Ultimate'), ('Melee', 'Melee'), ('Both', 'Both')])

    frontShell = StringField(
        validators=[DataRequired(), Length(max=20), AlphaSpace()])

    frontShellQual = RadioField(validators=[DataRequired()], choices=[
        ('Low', 'Low'), ('Mid', 'Mid'), ('High', 'High'), ('Very High', 'Very High')])

    backShell = StringField(
        validators=[DataRequired(), Length(max=20), AlphaSpace()])

    backShellQual = RadioField(validators=[DataRequired()], choices=[
        ('Low', 'Low'), ('Mid', 'Mid'), ('High', 'High'), ('Very High', 'Very High')])

    motherboard = RadioField(validators=[DataRequired()], choices=[(
        'OEM', 'OEM (50$, Nintendo standard, this includes snapback module, fresh potentiometers, and lubed triggers)')])

    grayStickbox = RadioField(validators=[DataRequired()], choices=[
        ('Factory New', 'Factory New ($15)'), ('A Tier', 'A Tier ($11)'), ('B Tier', 'B Tier ($2)')])

    cStickbox = RadioField(validators=[DataRequired()], choices=[
        ('Factory New', 'Factory New ($15)'), ('A Tier', 'A Tier ($11)'), ('B Tier', 'B Tier ($2)')])

    grayStickCap = RadioField(validators=[DataRequired()], choices=[
        ('Factory New', 'Factory New ($12)'), ('A Tier', 'A Tier ($7)'), ('B Tier', 'B Tier ($4)'), ('F Tier', 'F Tier (VERY WORN, FREE)')])

    cStickCap = RadioField(validators=[DataRequired()], choices=[
        ('Factory New', 'Factory New ($6)'), ('A Tier', 'A Tier ($3)'), ('B Tier', 'B Tier (FREE)')])

    upgrades = MultiCheckboxField(validators=[AtLeastOneChecked()], choices=[
        ('fnT3Bundle', 'Factory New T3 Bundle ($25, BEST VALUE, includes everything listed below)'), ('fnLowFricTrigPotent', 'Factory New Low Friction Trigger Potentiometers ($10)'), ('fnT3Motherboard', 'Factory New T3 Motherboard ($10)'), ('fnT3BtnTrigPads', 'Factory New T3 Button/Trigger Pads ($10)'), ('fnT3BtnTrigPieces', 'Factory New T3 Button/Trigger Pieces ($5)'), ('upgradeNone', 'None')])

    trigPotent = RadioField(validators=[DataRequired()], choices=[
        ('Factory New Low Friction', 'Factory New Low Friction ($10, does not double charge if selected above)'), ('Used', 'Used (FREE)')])

    btnTrigStickColor = RadioField(validators=[DataRequired()], choices=[
        ('Standard Gray', 'Standard Gray (FREE)'), ('Black Dyed OEM', 'Black Dyed OEM ($15, excludes sticks)'), ('Light Gray', 'Light Gray ($25, FREE with white shell combo)')])

    cord = RadioField(validators=[DataRequired()], choices=[
        ('Standard Black 2 Meter', 'Standard Black 2 Meter (FREE)'), ('Standard Black 3 Meter', 'Standard Black 3 Meter ($4, comes with black plug)'), ('White 3 Meter', 'White 3 Meter ($30, FREE with white shell combo)'), ('Paracord 2 Meter', 'Paracord 2 Meter ($35, any color of your choosing)'), ('Paracord 3 Meter', 'Paracord 3 Meter ($45, any color of your choosing)')])

    notches = RadioField(validators=[DataRequired()], choices=[
        ('Wavedash', 'Wavedash ($30)'), ('Firefox', 'Firefox ($120, includes wavedash)'), ('None', 'None (shield drop notches come for free automatically)')])

    buttonMods = MultiCheckboxField(validators=[AtLeastOneChecked()], choices=[
        ('baldBtns', 'Bald Buttons ($70, not compatible with Black Dyed OEM)'), ('stabilizedBtns', 'Stabilized Buttons ($4)'), ('zRemapX', 'Z Jump Remap Toggleable with X ($50, Swaps X and Z)'), ('zRemapY', 'Z Jump Remap Toggleable with Y ($50, Swaps Y and Z)'), ('tactileZ', 'Tactile Z ($10)'), ('btnNone', 'None')])

    shortPlug = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    longPlug = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    digTrigUltimateMelee = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    digTrigUltimate = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    stabilizedTrigs = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    shortenedSpring = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    removedSpring = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    rumbleMod = RadioField(validators=[DataRequired()], choices=[
        ('Regular', 'Regular (no modification, FREE)'), ('Disconnected Motor', "Disconnected Motor (motor weight remains but won't rumble, FREE)"), ('Removed Motor', 'Removed Motor (completely removes motor from shell, FREE)')])

    cordPlugColor = RadioField(validators=[DataRequired()], choices=[
        ('Default', 'Default (FREE, color that comes with your shell color)'), ('Indigo', 'Indigo ($5)'), ('Black', 'Black ($5)'), ('Orange', 'Orange ($5)'), ('Platinum', 'Platinum ($5)'), ('White', 'White ($25)'), ('Emerald', 'Emerald ($27)'), ('Luigi', 'Luigi ($30)'), ('Mario', 'Mario ($30)'), ('Club Nintendo', 'Club Nintendo ($30)'), ('Clear', 'Clear ($35)'), ('Panasonic', 'Panasonic ($50)'), ('Wario', 'Wario ($60)')])

    queueSkip = RadioField(validators=[DataRequired()], choices=[
        ('7 days', 'Ship within 7 days ($100)'), ('21 Days', 'Ship within 21 days ($50)'), ('49 Days', 'Ship within 49 days (FREE)')])

    firstLastName = StringField(validators=[DataRequired(), Length(max=30)])
    streetAddress = StringField(validators=[DataRequired(), Length(max=45)])
    city = StringField(
        validators=[DataRequired(), Length(max=20), AlphaSpaceHyphen()])
    state = StringField(
        validators=[DataRequired(), Length(max=20), AlphaSpace()])
    zipCode = StringField(
        validators=[DataRequired(), Length(max=15), ValidZipCode()])
    country = StringField(
        validators=[DataRequired(), Length(max=20), AlphaSpace()])

    readPriceGuide = RadioField(validators=[DataRequired()], choices=[(
        'I understand', 'Yes, I understand')])

    insurancePolicy = RadioField(validators=[DataRequired()], choices=[(
        'I understand', 'I have read the insurance policy and understand what is covered and what is not')])

    dmGio = RadioField(validators=[DataRequired()], choices=[(
        "DM'd", "Yes, I have DM'd, ready to submit!")])

    submit = SubmitField("Submit")


class Nine9Form(FlaskForm):

    formType = HiddenField("formType", default='99',
                           validators=[DataRequired(), AnyOf(['99'])])

    handle = StringField(validators=[DataRequired(), Length(max=38)])

    useCase = RadioField(validators=[DataRequired()], choices=[
        ('Ultimate', 'Ultimate'), ('Melee', 'Melee'), ('Both', 'Both')])

    color = RadioField(validators=[DataRequired()], choices=[
        ('Platinum', 'Platinum'), ('Orange', 'Orange'), (' Indigo', ' Indigo'), ('Black', 'Black')])

    grayStickbox = RadioField(validators=[DataRequired()], choices=[
        ('Factory New', 'Factory New ($15)'), ('A Tier', 'A Tier ($11)'), ('No Upgrade', 'No Upgrade')])

    cStickbox = RadioField(validators=[DataRequired()], choices=[
        ('Factory New', 'Factory New ($15)'), ('A Tier', 'A Tier ($11)'), ('No Upgrade', 'No Upgrade')])

    grayStickCap = RadioField(validators=[DataRequired()], choices=[
        ('Factory New', 'Factory New ($12)'), ('A Tier', 'A Tier ($7)'), ('B Tier', 'B Tier ($4)'), ('Default', 'Default (D/F Tier, VERY WORN, FREE)')])

    cStickCap = RadioField(validators=[DataRequired()], choices=[
        ('Factory New', 'Factory New ($6)'), ('A Tier', 'A Tier ($3)'), ('Default', 'Default (B Tier, FREE)')])

    upgrades = MultiCheckboxField(validators=[AtLeastOneChecked()], choices=[
        ('fnT3Bundle', 'Factory New T3 Bundle ($25, BEST VALUE, includes everything listed below)'), ('fnLowFricTrigPotent', 'Factory New Low Friction Trigger Potentiometers ($10)'), ('fnT3Motherboard', 'Factory New T3 Motherboard ($10)'), ('fnT3BtnTrigPads', 'Factory New T3 Button/Trigger Pads ($10)'), ('fnT3BtnTrigPieces', 'Factory New T3 Button/Trigger Pieces ($5)'), ('upgradeNone', 'None')])

    trigPotent = RadioField(validators=[DataRequired()], choices=[
        ('Factory New Low Friction', 'Factory New Low Friction ($10, does not double charge if selected above)'), ('No Upgrade', 'No Upgrade')])

    btnTrigStickColor = RadioField(validators=[DataRequired()], choices=[
        ('Standard Gray', 'Standard Gray (FREE)'), ('Black Dyed OEM', 'Black Dyed OEM ($15, excludes sticks)'), ('Light Gray', 'Light Gray ($25)')])

    cord = RadioField(validators=[DataRequired()], choices=[
        ('Standard Black 2 Meter', 'Standard Black 2 Meter (FREE)'), ('Standard Black 3 Meter', 'Standard Black 3 Meter ($4, comes with black plug)'), ('White 3 Meter', 'White 3 Meter ($30)'), ('Paracord 2 Meter', 'Paracord 2 Meter ($35, any color of your choosing)'), ('Paracord 3 Meter', 'Paracord 3 Meter ($45, any color of your choosing)')])

    notches = RadioField(validators=[DataRequired()], choices=[
        ('Wavedash', 'Wavedash ($30)'), ('Firefox', 'Firefox ($120, includes wavedash)'), ('None', 'None (shield drop notches come for free automatically)')])

    buttonMods = MultiCheckboxField(validators=[AtLeastOneChecked()], choices=[
        ('baldBtns', 'Bald Buttons ($70, not compatible with Black Dyed OEM)'), ('stabilizedBtns', 'Stabilized Buttons ($4)'), ('zRemapX', 'Z Jump Remap Toggleable with X ($50, Swaps X and Z)'), ('zRemapY', 'Z Jump Remap Toggleable with Y ($50, Swaps Y and Z)'), ('tactileZ', 'Tactile Z ($10)'), ('btnNone', 'None')])

    shortPlug = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    longPlug = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    digTrigUltimateMelee = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    digTrigUltimate = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    stabilizedTrigs = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    shortenedSpring = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    removedSpring = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    rumbleMod = RadioField(validators=[DataRequired()], choices=[
        ('Regular', 'Regular (no modification, FREE)'), ('Disconnected Motor', "Disconnected Motor (motor weight remains but won't rumble, FREE)"), ('Removed Motor', 'Removed Motor (completely removes motor from shell, FREE)')])

    queueSkip = RadioField(validators=[DataRequired()], choices=[
        ('7 days', 'Ship within 7 days ($100)'), ('21 Days', 'Ship within 21 days ($50)'), ('49 Days', 'Ship within 49 days (FREE)')])

    firstLastName = StringField(validators=[DataRequired(), Length(max=30)])
    streetAddress = StringField(validators=[DataRequired(), Length(max=45)])
    city = StringField(
        validators=[DataRequired(), Length(max=20), AlphaSpaceHyphen()])
    state = StringField(
        validators=[DataRequired(), Length(max=20), AlphaSpace()])
    zipCode = StringField(
        validators=[DataRequired(), Length(max=15), ValidZipCode()])
    country = StringField(
        validators=[DataRequired(), Length(max=20), AlphaSpace()])

    readPriceGuide = RadioField(validators=[DataRequired()], choices=[(
        'I understand', 'Yes, I understand')])

    insurancePolicy = RadioField(validators=[DataRequired()], choices=[(
        'I understand', 'I have read the insurance policy and understand what is covered and what is not')])

    dmGio = RadioField(validators=[DataRequired()], choices=[(
        "DM'd", "Yes, I have DM'd, ready to submit!")])

    submit = SubmitField("Submit")


class One69Form(FlaskForm):

    formType = HiddenField("formType", default='169',
                           validators=[DataRequired(), AnyOf(['169'])])

    phobWarningX = RadioField(validators=[DataRequired()], choices=[
        ('I understand', 'I understand the risks associated with using a Phob on the Nintendo Switch')])

    handle = StringField(validators=[DataRequired(), Length(max=38)])

    useCase = RadioField(validators=[DataRequired()], choices=[
        ('Ultimate', 'Ultimate'), ('Melee', 'Melee'), ('Both', 'Both')])

    grayStickbox = RadioField(validators=[DataRequired()], choices=[
        ('Factory New', 'Factory New ($15)'), ('A Tier', 'A Tier ($11)'), ('No Upgrade', 'No Upgrade')])

    cStickbox = RadioField(validators=[DataRequired()], choices=[
        ('Factory New', 'Factory New ($15)'), ('A Tier', 'A Tier ($11)'), ('No Upgrade', 'No Upgrade')])

    grayStickCap = RadioField(validators=[DataRequired()], choices=[
        ('Factory New', 'Factory New ($12)'), ('A Tier', 'A Tier ($7)'), ('B Tier', 'B Tier ($4)'), ('Default', 'Default (C/D Tier, WORN, FREE)')])

    cStickCap = RadioField(validators=[DataRequired()], choices=[
        ('Factory New', 'Factory New ($6)'), ('A Tier', 'A Tier ($3)'), ('Default', 'Default (B Tier, FREE)')])

    upgrades = MultiCheckboxField(validators=[AtLeastOneChecked()], choices=[
        ('fnT3Bundle', 'Factory New T3 Bundle ($25 includes everything listed below)'), ('fnLowFricTrigPotent', 'Factory New Low Friction Trigger Potentiometers ($10)'), ('fnT3BtnTrigPads', 'Factory New T3 Button/Trigger Pads ($10)'), ('fnT3BtnTrigPieces', 'Factory New T3 Button/Trigger Pieces ($5)'), ('upgradeNone', 'None')])

    trigPotent = RadioField(validators=[DataRequired()], choices=[
        ('Factory New', 'Factory New ($10, does not double charge if selected above)'), ('No Upgrade', 'No Upgrade')])

    btnTrigStickColor = RadioField(validators=[DataRequired()], choices=[
        ('Standard Gray', 'Standard Gray (FREE)'), ('Black Dyed OEM', 'Black Dyed OEM ($15, excludes sticks)'), ('Light Gray', 'Light Gray ($25)')])

    cord = RadioField(validators=[DataRequired()], choices=[
        ('Standard Black 3 Meter', 'Standard Black 3 Meter (FREE)'), ('White 3 Meter', 'White 3 Meter ($30)'), ('Paracord 2 Meter', 'Paracord 2 Meter ($35, any color of your choosing)'), ('Paracord 3 Meter', 'Paracord 3 Meter ($45, any color of your choosing)')])

    notches = RadioField(validators=[DataRequired()], choices=[
        ('Wavedash', 'Wavedash ($24)'), ('Firefox', 'Firefox ($96, includes wavedash)'), ('None', 'None (shield drop notches come for free automatically)')])

    buttonMods = MultiCheckboxField(validators=[AtLeastOneChecked()], choices=[
        ('baldBtns', 'Bald Buttons ($70, not compatible with Black Dyed OEM and Mouse Click ABXY)'), ('mouseClickABXY', 'Mouse Click ABXY ($70, includes stabilized buttons for free, not compatible with bald buttons)'), ('stabilizedBtns', 'Stabilized Buttons ($4)'), ('zRemapX', 'Z Jump Remap Toggleable with X (FREE, pick one for me to swap, you can swap anytime)'), ('zRemapY', 'Z Jump Remap Toggleable with Y (FREE, pick one for me to swap, you can swap anytime)'), ('btnNone', 'None')])

    mouseClickTrig = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    shortPlug = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    longPlug = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    digTrigUltimate = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    stabilizedTrigs = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    shortenedSpring = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    removedSpring = MultiCheckboxField(validators=[AtMostOneChecked()], choices=[
        ('Left'), ('Right'), ('Both')])

    rumbleMod = RadioField(validators=[DataRequired()], choices=[
        ('Regular', 'Regular (no modification, FREE)'), ('Disconnected Motor', "Disconnected Motor (motor weight remains but won't rumble, FREE)"), ('Removed Motor', 'Removed Motor (completely removes motor from shell, FREE)')])

    queueSkip = RadioField(validators=[DataRequired()], choices=[
        ('7 days', 'Ship within 7 days ($100)'), ('21 Days', 'Ship within 21 days ($50)'), ('49 Days', 'Ship within 49 days (FREE)')])

    firstLastName = StringField(validators=[DataRequired(), Length(max=30)])
    streetAddress = StringField(validators=[DataRequired(), Length(max=45)])
    city = StringField(
        validators=[DataRequired(), Length(max=20), AlphaSpaceHyphen()])
    state = StringField(
        validators=[DataRequired(), Length(max=20), AlphaSpace()])
    zipCode = StringField(
        validators=[DataRequired(), Length(max=15), ValidZipCode()])
    country = StringField(
        validators=[DataRequired(), Length(max=20), AlphaSpace()])

    readPriceGuide = RadioField(validators=[DataRequired()], choices=[(
        'I understand', 'Yes, I understand')])

    insurancePolicy = RadioField(validators=[DataRequired()], choices=[(
        'I understand', 'I have read the insurance policy and understand what is covered and what is not')])

    dmGio = RadioField(validators=[DataRequired()], choices=[(
        "DM'd", "Yes, I have DM'd, ready to submit!")])

    submit = SubmitField("Submit")
