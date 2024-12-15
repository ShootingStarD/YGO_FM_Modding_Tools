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

convert_card_drop_plan_into_drop_excel : The convert card drop plan into drop excel allows you to fill the Card Drop Plan template (which specifies each card an rank of an opponent can give) to get the corresponding drop_template where cards drop in the same rank of the same oppenents have the same probabilities to drop. Such drop template can then be fed in the [TeaOnline Drop Data tool](https://www.basededatostea.xyz/extend/tools/drop) to get SLUS and WRA files to build the modded ISO
