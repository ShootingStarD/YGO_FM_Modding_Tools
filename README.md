# YGO_FM_Modding_Tools

Tools and scripts to mod more easily YGO Forbidden Memories

The tools are intended to automate creations of template that can be used in [TeaOnline](https://www.basededatostea.xyz/extend/tools) to mod YGO Forbidden Memories

## Install

```bash
git clone https://github.com/ShootingStarD/YGO_FM_Modding_Tools
cd YGO_FM_Modding_Tools
python -m venv .venv #create virtual env
source .venv/bin/activate
pip install .
```

## Scripts

### card_list.py

Downloads the whole card list of the game from [yugipedia](https://yugipedia.com/wiki/List_of_Yu-Gi-Oh!_Forbidden_Memories_cards) into a csv file : card_list.csv
The picture column is the url of the in-game card picture

### convert_card_drop_plan_into_drop_excel.py

convert_card_drop_plan_into_drop_excel : The convert card drop plan into drop excel allows you to fill the Card Drop Plan template (which specifies each card an rank of an opponent can give) to get the corresponding drop_template where cards drop in the same rank of the same opponents have the same probabilities to drop. Such drop template can then be fed in the [TeaOnline Drop Data tool](https://www.basededatostea.xyz/extend/tools/drop) to get SLUS and WRA files to build the modded ISO

## YGO FM Rebalanced

YGO FM Rebalanced is a Mod made to keep the spirit of the original game, while making farming and beating the game without cheats, 15 cards drop or speedup more bearable. For this, the following changes have been made :

- Campaign Drop : Each character gives a specific card once you beat it for the first time in the campaign. The cards are often reminiscent of their theme or a card they use in the anime/manga. For example Jono 2nd gives the Red Eyes Black Dragon while Seto 3rd gives the Blues Eyes White Dragon.
- Drop Rebalanced : Drops have been rebalanced to gives way more easily powerful cards. Most drops are chosen to be coherent with the anime, structure deck or theme of the duelist. For example Jono 1 gives most low level warrior and beast warrior as well as some pyro's monster for the Flame Swordman. Each mage and archmage give the strongest cards with ATK < 3000 for their respective field affected monster (for example Ocean Mage gives the 2 headed thunder dragon and aqua drago , desert mage gives the gold mammoth and the summoned skull (because it is a skull)). Mai and Tea 1 and Tea 2 give all female cards except the cosmo queen (which Heinshin will drop).  S/A tec only gives magic and trap card. You therefore have to do way less S/A tec to get valuable non monsters card.
- More Fusions : Moth line can be fused using the Cocoon of Evolution. BLS and Magician of Black Chaos can be obtained by fusion and others
- Equip Reworked : Some equips compatibilities were changed. Now the BLS can use the Legendary Sword, B Skull Dragon can use all equips of Summoned Skull.

The modded ISO can be downloaded [here](https://www.mediafire.com/file/5syvxx5v9plx58q/YGO_FM_Rebalanced.iso/file)

See Card Drop Plan xlsx for full card drop plan as well as Campaign drop (second sheet). update_drop_template.xlsx is the excel file used to feed the [drop modifying in tea online](https://www.basededatostea.xyz/extend/tools/drop)

In your ISO, replace the SLUS and WA_MRG file by those of the repo to get the modded game