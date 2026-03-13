# 字段字典

| 表 | 字段 | 非空率 | 唯一值数量 | 示例值 |
|---|---|---:|---:|---|
| ActionTable | TID | 0.9524 | 20 | 区分字, U16, 1 |
| ActionTable | EngName | 0.9524 | 20 | 英文名(32字), CBwString, ACT_000001 |
| ActionTable | LocalName | 0.9524 | 20 | 韩文名(32字), CBwString, 常规项目 |
| ActionTable | Type | 0.9524 | 6 | 类型, U8, 1 |
| ActionTable | SkillTID | 0.9524 | 20 | 技能 TID 号码, U32, 232011 |
| ActionTable | Icon | 0.9524 | 13 | 图标, U32, 0 |
| ActionTable | EndType | 0.9524 | 5 | ani结束后角色的状态进行处理 0: 结束持续 1: 结束后闲置 2: 循环, U8, 0 |
| ActionTable | Desc | 0.9048 | 16 | 社会信息, CBwString:v, WORD_COLLECTING |
| AreaTable | TID | 0.9986 | 1425 | U32, 1, 2 |
| AreaTable | Type | 0.9986 | 3 | U32, 1, 0 |
| AreaTable | Kind | 0.9986 | 4 | U32, 0, 1 |
| AreaTable | WeatherUse | 0.9986 | 3 | U32, 1, 0 |
| AreaTable | WorldTID | 0.9986 | 156 | U32, 10001, 1 |
| AreaTable | GroupNum | 0.9986 | 3 | U16, 0, 1 |
| AreaTable | D_X | 0.9986 | 1025 | F32, 0, 128 |
| AreaTable | D_Y | 0.9986 | 1021 | F32, 0, 128 |
| AreaTable | D_Z | 0.9986 | 987 | F32, 0, 165.3 |
| AreaTable | Radius | 0.9986 | 45 | F32, 32, 128 |
| AreaTable | AimRebirthPos | 0.0252 | 32 | F32:v, 256.55|206.63|162.68, 134.22|345.30|-1.54 |
| AreaTable | DemolRebirthPos | 0.0196 | 26 | F32:v, 259.24|175.50|152.77, 374.94|194.75|-1.43 |
| AreaTable | Comment | 0.1906 | 263 | CBwString, 洛坎的实验室:普通, 洛坎的实验室:困难 |
| AreaTable | EngName | 0.9748 | 1391 | CBwString, ART_Name_000001, ART_Name_000002 |
| AreaTable | EngSubName | 0.9748 | 1391 | CBwString, ART_Subname_000001, ART_Subname_000002 |
| AreaTable | LocalName | 0.8262 | 510 | CBwString, 角色工具, 角色生成 |
| AreaTable | LocalSubName | 0.5473 | 516 | CBwString, 高精准, 破坏 |
| AreaTable | BgmName | 0.1331 | 39 | CBwString:v, Sound/BGM/BGM_02.ogg, Sound/BGM/BGM_04.ogg |
| AreaTable | BgmLoop | 0.9986 | 3 | U16, 0, 1 |
| AreaTable | Weather0 | 0.1864 | 82 | CBwString, 3013|4045|, 3029|4034| |
| AreaTable | Weather1 | 0.1864 | 89 | CBwString, 3013|4045|, 3029|4034| |
| AreaTable | Weather2 | 0.1864 | 86 | CBwString, 3013|4045|, 3029|4034| |
| AreaTable | Weather3 | 0.1864 | 80 | CBwString, 3013|4045|, 3029|4034| |
| BanWordTable | TID | 1.0 | 2825 | 区分字, 2, U16 |
| BanWordTable | Type | 0.9996 | 3 | 类型, U8, 3 |
| BanWordTable | String | 0.9996 | 2824 | 禁止语, CBwString, 毛泽东 |
| CashShopInfo | TID | 0.9935 | 152 | TID, U16, 1 |
| CashShopInfo | VER | 0.9935 | 3 | АцБО, U16, 0 |
| CashShopInfo | Type | 0.9935 | 3 | БъЧЉРраЭ, U8, 1 |
| CashShopInfo | SubType | 0.9935 | 8 | БъЧЉзгРраЭ, U8, 1 |
| CashShopInfo | ItemId | 0.9935 | 152 | ЕРОпID, U32, 90000 |
| CashShopInfo | ItemNum | 0.9935 | 4 | Ъ§СП, U16, 1 |
| CashShopInfo | OnceNum | 0.9935 | 4 | вЛДЮЙКТђЪ§СП, U16, 2 |
| CashShopInfo | CastType | 0.9935 | 3 | жЇИЖРраЭ, U8, 0 |
| CashShopInfo | CastNum | 0.9935 | 29 | жЇИЖМлИё, U32, 5000 |
| CashShopInfo | Discount | 0.9935 | 3 | елПл, U8, 100 |
| CharBaseInfoTable | TID | 1.0 | 11 | 人物ID, 0, U16 |
| CharBaseInfoTable | Race | 1.0 | 7 | 种族, 0, U8 |
| CharBaseInfoTable | Gen | 1.0 | 5 | 性别, 0, U8 |
| CharBaseInfoTable | MapID | 1.0 | 4 | 地图ID, 0, U32 |
| CharBaseInfoTable | Weapon_Shield | 1.0 | 5 | 盾, 0, U32:a:Weapon |
| CharBaseInfoTable | Weapon_Lance | 0.6364 | 4 | 矛, 0, U32 |
| CharBaseInfoTable | Weapon_Staff | 0.6364 | 4 | 随从, 0, U32 |
| CharBaseInfoTable | Weapon_Axe | 0.4545 | 4 | 斧子, 0, U32 |
| CharBaseInfoTable | Weapon_Bow | 0.6364 | 4 | 弓, 0, U32 |
| CharBaseInfoTable | Weapon_Charkram | 0.2727 | 3 | 能源, 0, U32 |
| CharBaseInfoTable | Weapon_Cannon | 0.2727 | 3 | 大炮, 0, U32 |
| CharBaseInfoTable | Weapon_Dagger | 0.2727 | 3 | 尖刀, 0, U32 |
| CharBaseInfoTable | Weapon_Orb | 0.4545 | 4 | 天体, 0, U32 |
| CharBaseInfoTable | Weapon_MagicGun | 0.4545 | 4 | 马坦枪, 0, U32 |
| CharBaseInfoTable | Weapon_Sword | 0.6364 | 4 | 单手剑, 0, U32 |
| CharBaseInfoTable | Weapon_Blade | 0.4545 | 4 | 双手剑, 0, U32 |
| CharBaseInfoTable | Weapon_Arbalest | 0.6364 | 4 | 剑弩, 0, U32 |
| CharBaseInfoTable | Weapon_Wand | 0.6364 | 4 | 权杖, 0, U32 |
| CharBaseInfoTable | Skill_Shield | 0.2727 | 3 | 盾牌技能, 0, U32:a:Skill |
| CharBaseInfoTable | Skill_Lance | 0.6364 | 4 | 矛技能, 0, U32 |
| CharBaseInfoTable | Skill_Staff | 0.6364 | 4 | 随从技能, 0, U32 |
| CharBaseInfoTable | Skill_Axe | 0.4545 | 4 | 斧子技能, 0, U32 |
| CharBaseInfoTable | Skill_Bow | 0.6364 | 4 | 弓技能, 0, U32 |
| CharBaseInfoTable | Skill_Charkram | 0.2727 | 3 | 能源技能, 0, U32 |
| CharBaseInfoTable | Skill_Cannon | 0.2727 | 3 | 大炮技能, 0, U32 |
| CharBaseInfoTable | Skill_Dagger | 0.2727 | 3 | 尖刀技能, 0, U32 |
| CharBaseInfoTable | Skill_Orb | 0.4545 | 4 | 天体技能, 0, U32 |
| CharBaseInfoTable | Skill_MagicGun | 0.4545 | 4 | 马坦枪技能, 0, U32 |
| CharBaseInfoTable | Skill_Sword | 0.6364 | 4 | 单手剑技能, 0, U32 |
| CharBaseInfoTable | Skill_Blade | 0.4545 | 4 | 双手剑技能, 0, U32 |
| CharBaseInfoTable | Skill_Arbalest | 0.6364 | 4 | 剑弩技能, 0, U32 |
| CharBaseInfoTable | Skill_Wand | 0.6364 | 4 | 权杖技能, 0, U32 |
| CharBaseInfoTable | StartLV | 0.9091 | 3 | 入门级别, U8, 1 |
| CharBaseInfoTable | StartWLV | 0.9091 | 3 | 入门武器, U8, 1 |
| CharBaseInfoTable | StartItem | 0.9091 | 4 | 付款, U32:v, 9083|9000|9010|9040|9020 |
| CharBaseInfoTable | StartItemCnt | 0.9091 | 3 | 付款额, U32:v, 1|10|10|5|3 |
| CharBaseInfoTable | StartItemQuick | 0.9091 | 3 | 快速支付模块号码, U8:v, 0|4|5|0|0 |
| CharBaseInfoTable | ArchLordSkill | 0.9091 | 3 | 霸王专属技能, U32:v, 233011|233021|233031|233041|233051|233061|233071|233081 |
| CharBaseInfoTable | LimitAS | 0.9091 | 3 | 最高攻击速度, S16, 32000 |
| CharBaseInfoTable | LimitRS | 0.9091 | 3 | 最高移动速度, S16, 32000 |
| CharBlendAniTable | TID | 1.0 | 10 | 分离器, 2, U8 |
| CharBlendAniTable | Priority | 0.9091 | 4 | 优先区域, S32, 2 |
| CharBlendAniTable | Weight | 0.9091 | 3 | 重量, F32, 1 |
| CharBlendAniTable | EaseInTime | 0.9091 | 7 | 加入Ani运动时的状态, F32, 0.15 |
| CharBlendAniTable | Deactivate | 0.9091 | 7 | 加入Ani静止时的状态, F32, 0.15 |
| CharBlendAniTable | Desc | 0.9091 | 10 | 说明, CBwString, Skill |
| CharEffectTable | CharName | 1.0 | 321 | 2, CBwString, #Share |
| CharEffectTable | Kind | 1.0 | 7 | 2, U8, 0 |
| CharEffectTable | EffectName | 0.9196 | 3516 | 2, CBwString, FX_ice_a |
| CharEffectTable | ResourceName | 0.7851 | 1788 | 2, string, FOOT/FX_ICE_A.NIF |
| CharEffectTable | NodeName | 1.0 | 185 | 2, CBwString, Bip01 L Foot |
| CharEffectTable | SequenceID | 1.0 | 389 | 2, U32, 0 |
| CharEffectTable | StartTime | 1.0 | 1723 | 2, F32, 0 |
| CharEffectTable | TimeLength | 1.0 | 75 | 2, F32, 1 |
| CharEffectTable | TX | 1.0 | 2842 | 2, F32, -11.921 |
| CharEffectTable | TY | 1.0 | 4256 | 2, F32, 0 |
| CharEffectTable | TZ | 1.0 | 4382 | 2, F32, 5.945 |
| CharEffectTable | RX | 1.0 | 1815 | 2, F32, 0 |
| CharEffectTable | RY | 1.0 | 1448 | 2, F32, 0 |
| CharEffectTable | RZ | 1.0 | 2187 | 2, F32, 0 |
| CharEffectTable | Scale | 1.0 | 916 | 2, F32, 1 |
| CharEffectTable | Flags | 1.0 | 44 | 2, U32, 0 |
| CharEffectTable | ActiveMode | 1.0 | 5 | 2, U32, 1 |
| CharEffectTable | DeActiveMode | 1.0 | 6 | 2, U32, 1 |
| CharEffectTable | DirMode | 1.0 | 4 | 2, U32, 0 |
| CharEffectTable | ActiveEvent | 1.0 | 28 | 2, U32, 29 |
| CharEffectTable | DeActiveEvent | 1.0 | 16 | 2, U32, 0 |
| CharEffectTable | Extend | 0.1255 | 98 | 2, CBwString, dangerfx:(S_BG)PC危险警报效果|dangerfxalpha:(S_BG)PC危险警报效果| |
| CharEffectTable_Sound | CharName | 0.9999 | 237 | 2, CBwString, #Share |
| CharEffectTable_Sound | Kind | 0.9999 | 3 | 2, U8, 1 |
| CharEffectTable_Sound | EffectName | 0.6942 | 1307 | 2, CBwString, selected_enemy |
| CharEffectTable_Sound | ResourceName | 0.9994 | 3766 | 2, string, SYSTEM/SYSTEM_TARGET_SELECTED_01.OGG |
| CharEffectTable_Sound | NodeName | 0.9999 | 4 | 2, CBwString, Bone_Root |
| CharEffectTable_Sound | SequenceID | 0.9999 | 302 | 2, U32, 0 |
| CharEffectTable_Sound | StartTime | 0.9999 | 1736 | 2, F32, 0 |
| CharEffectTable_Sound | TimeLength | 0.9999 | 4 | 2, F32, 1 |
| CharEffectTable_Sound | TX | 0.9999 | 42 | 2, F32, 0 |
| CharEffectTable_Sound | TY | 0.9999 | 23 | 2, F32, 0 |
| CharEffectTable_Sound | TZ | 0.9999 | 7 | 2, F32, 0 |
| CharEffectTable_Sound | RX | 1.0 | 7 | MinDist(Sound), 2, F32 |
| CharEffectTable_Sound | RY | 1.0 | 14 | MaxDist, 2, F32 |
| CharEffectTable_Sound | RZ | 0.9999 | 3 | 2, F32, 0 |
| CharEffectTable_Sound | Scale | 0.9999 | 101 | 2, F32, 1 |
| CharEffectTable_Sound | Flags | 0.9999 | 6 | 2, U32, 1 |
| CharEffectTable_Sound | ActiveMode | 0.9999 | 4 | 2, U32, 1 |
| CharEffectTable_Sound | DeActiveMode | 0.9999 | 5 | 2, U32, 3 |
| CharEffectTable_Sound | DirMode | 0.9999 | 3 | 2, U32, 0 |
| CharEffectTable_Sound | ActiveEvent | 0.9999 | 15 | 2, U32, 12 |
| CharEffectTable_Sound | DeActiveEvent | 0.9999 | 7 | 2, U32, 13 |
| CharEffectTable_Sound | Extend | 0.0001 | 2 | 2, CBwString |
| CharFigureTable | TID | 1.0 | 67 | 롸잼포, 2, U32 |
| CharFigureTable | CharID | 1.0 | 11 | 훙膠ID, 2, U32 |
| CharFigureTable | Name | 1.0 | 20 | 檎츰, 2, CBwString |
| CharFigureTable | BoneList | 0.9559 | 65 | 湳굶헌데, 2, CBwString |
| CharShapeTable | ID | 1.0 | 960 | 人物ID, 2, U32 |
| CharShapeTable | MediaPath | 1.0 | 6 | 网络文件位置, 2, string |
| CharShapeTable | Bone | 1.0 | 388 | 模特名, 2, string |
| CharShapeTable | MPartsFace | 0.3444 | 80 | 脸部文件名, 2, string:a:MParts |
| CharShapeTable | MPartsEyeball | 0.18 | 31 | 眼球文件名, 2, string |
| CharShapeTable | MPartsHair | 0.3444 | 67 | 头发颜色文件名, 2, string |
| CharShapeTable | MPartsHelm | 0.1717 | 135 | 头盔文件名, 2, string |
| CharShapeTable | MPartsBody | 0.8325 | 570 | 上体文件名, 2, string |
| CharShapeTable | MPartsHand | 0.18 | 143 | 小臂文件名, 2, string |
| CharShapeTable | MPartsLegs | 0.1675 | 23 | 下体文件名, 2, string |
| CharShapeTable | MPartsFoot | 0.18 | 143 | 长筒靴文件名, 2, string |
| CharShapeTable | MPartsCape | 0.0219 | 15 | 披风文件名, 2, string |
| CharShapeTable | LHandWeapon | 0.205 | 46 | 左手武器, 2, string:v |
| CharShapeTable | RHandWeapon | 0.3101 | 89 | 右手武器, 2, string:v |
| CharShapeTable | ItemMeshScale | 0.0021 | 2 | 武器尺码, F32 |
| CharShapeTable | StepLOD_01 | 1.0 | 6 | 1阶段 LOD, 2, F32:a:StepLOD |
| CharShapeTable | StepLOD_02 | 1.0 | 6 | 2阶段 LOD, 2, F32 |
| CharShapeTable | StepLOD_03 | 1.0 | 6 | 3阶段 LOD, 2, F32 |
| CharShapeTable | StepLOD_04 | 1.0 | 6 | 4阶段 LOD, 2, F32 |
| CharShapeTable | StepLOD_05 | 1.0 | 6 | 5阶段 LOD, 2, F32 |
| CharShapeTable | EffectCreate | 0.0884 | 84 | 创作效果, 2, CBwString |
| CharShapeTable | HitEffectKind | 0.999 | 5 | 打击效果, 2, U8 |
| CharShapeTable | FourFoot | 0.999 | 5 | 4步, 2, U8 |
| ChatTable | TID | 1.0 | 16 | 分离器, 2, U8 |
| ChatTable | EngDesc | 0.9412 | 16 | 英文说明, CBwString, CHT_Desc_000001 |
| ChatTable | LocalDesc | 0.9412 | 16 | 说明, CBwString, 一般频道 |
| ChatTable | Type | 0.9412 | 16 | 种类(0=一般, 1=队伍频道,2=公众频道,3=工会频道,4=喊,5=悄悄话,6=战斗,7=系统,8=控制), U8, 0 |
| ChatTable | RGB | 0.9412 | 15 | RGB 价格, CBwString, <TC '255:255:255' /> |
| ChatTable | ChannelName | 0.9412 | 11 | 频道名 (信息标签  StringID 使用), CBwString, WORD_CHAT_GENERAL |
| ChatTable | Normal | 0.8824 | 9 | 一般标签按钮(1=转账,2=队伍,3=工会,4=战斗,5=系统), U8:v, 1 |
| ChatTable | EngHotKey_01 | 0.8824 | 15 | CBwString, CHT_Hotkey01_000001, CHT_Hotkey01_000002 |
| ChatTable | LocalHotKey_01 | 0.6471 | 11 | 1#快捷键, CBwString, s |
| ChatTable | EngHotKey_02 | 0.8824 | 15 | CBwString, CHT_Hotkey02_000001, CHT_Hotkey02_000002 |
| ChatTable | LocalHotKey_02 | 0.6471 | 11 | 2#快捷键, CBwString, s |
| ChatTable | AvailChat | 0.9412 | 14 | 可用的聊天, U8, 0 |
| CommandTable | TID | 0.9831 | 116 | U16, 1, 2 |
| CommandTable | Category | 0.9915 | 23 | ЪЙгУЖдЯѓЧјЗж, CBwString, PC |
| CommandTable | Type | 0.9915 | 4 | ЗўЮёЦї1, ПЫР­2, U8, 1 |
| CommandTable | UserAuth | 0.9915 | 4 | ЪЙгУШЈЯо(0=Юо,1=гУЛЇПЩгУ, 2= дЫгЊЩЬПЩгУ, 3=ПЊЗЂепПЩгУ), U8, 3 |
| CommandTable | LocalCommand | 0.9915 | 116 | КЋгя(КЋгявВПЩЫЕУї), CBwString, /m |
| CommandTable | EngCommand | 0.9068 | 106 | гЂЮФ, CBwString, /m |
| CommandTable | Desc | 0.9831 | 114 | ЫЕУї, CBwString, PC ЫРЭі |
| CommandTable | Arg_Num | 0.9831 | 6 | U8, 0, 1 |
| CommandTable | Arg1 | 0.5763 | 24 | CBwString, ГЃЪ§жЕ, ГЃЪ§жЕ(+,-) |
| CommandTable | Arg2 | 0.1186 | 11 | CBwString, x зјБъ, НћжЙ ЪБМф |
| CommandTable | Arg3 | 0.0339 | 3 | CBwString, y зјБъ, ГЃЪ§жЕ |
| CommandTable | Arg4 | 0.0254 | 2 | CBwString, z зјБъ |
| CommandTable | InputEx | 0.661 | 78 | ДэЮѓЕФаХЯЂЪфГі, CBwString, вЦЖЏ [ЧјгђУћзж]вЦЖЏ [ЧјгђID]вЦЖЏ [X] [Y] [Z]вЦЖЏ [X] [Y] [Z] [ЧјгђID] |
| ContentsOptionTable | TID | 0.9286 | 13 | TID, U32, 1 |
| ContentsOptionTable | mSvrNo | 0.9286 | 3 | 服务器编号, U32, 0 |
| ContentsOptionTable | mOptionNo | 0.9286 | 13 | 内容编号, U8, 1 |
| ContentsOptionTable | mOptionNm | 0.9286 | 13 | 内容名称, CBwString, 游戏内限制 |
| ContentsOptionTable | mOptionDesc | 0.9286 | 13 | 内容说明, CBwString, PC, 武器熟练度, Pc 仓库/ 库存, 公会 仓库保管Ghelld使用限制 |
| ContentsOptionTable | mOptionDesc0 | 0.9286 | 12 | 选项说明0, CBwString, PC等级限制 |
| ContentsOptionTable | mOptionValue0 | 0.7857 | 9 | 选项值0, F32, 60 |
| ContentsOptionTable | mOptionDesc1 | 0.8571 | 12 | 选项说明1, CBwString, 主武器熟练度等级限制 |
| ContentsOptionTable | mOptionValue1 | 0.7857 | 11 | 选项值1, F32, 60 |
| ContentsOptionTable | mOptionDesc2 | 0.7857 | 11 | 选项说明2, CBwString, 辅助武器熟练度等级限制 |
| ContentsOptionTable | mOptionValue2 | 0.7857 | 11 | 选项值2, F32, 60 |
| ContentsOptionTable | mOptionDesc3 | 0.7143 | 10 | 选项说明3, CBwString, 库存保管的金额限制 |
| ContentsOptionTable | mOptionValue3 | 0.6429 | 9 | 选项值3, F32, 1000000000 |
| ContentsOptionTable | mOptionDesc4 | 0.7143 | 10 | 选项说明4, CBwString, PC仓库保管金额限制 |
| ContentsOptionTable | mOptionValue4 | 0.7143 | 9 | 选项值4, F32, 1000000000 |
| ContentsOptionTable | mOptionDesc5 | 0.6429 | 9 | 选项说明5, CBwString, 公会仓库保管金额限制 |
| ContentsOptionTable | mOptionValue5 | 0.6429 | 8 | 选项值5, F32, 1000000000 |
| ContentsOptionTable | mOptionDesc6 | 0.6429 | 9 | 选项说明6, CBwString, 公会创立费用 |
| ContentsOptionTable | mOptionValue6 | 0.5714 | 7 | 选项值6, F32, 200000 |
| ContentsOptionTable | mOptionDesc7 | 0.6429 | 9 | 选项说明7, CBwString, 公会创立等级限制 |
| ContentsOptionTable | mOptionValue7 | 0.5714 | 7 | 选项值7, F32, 20 |
| ContentsOptionTable | mOptionDesc8 | 0.5714 | 8 | 选项说明8, CBwString, 公会贡献度。 |
| ContentsOptionTable | mOptionValue8 | 0.5714 | 6 | 选项值8, F32, 100 |
| ContentsOptionTable | mOptionDesc9 | 0.5714 | 7 | 选项说明9, CBwString, 阵容相比最小的设定数 |
| ContentsOptionTable | mOptionValue9 | 0.5714 | 7 | 选项值9, F32, 500 |
| ContentsOptionTable | mOptionDesc10 | 0.2857 | 4 | 选项说明10, CBwString, 阵营间比率 |
| ContentsOptionTable | mOptionValue10 | 0.2857 | 4 | 选项值10, F32, 60 |
| ContentsOptionTable | mOptionDesc11 | 0.2857 | 4 | 选项说明11, CBwString, 种族电脑生成的限制 |
| ContentsOptionTable | mOptionValue11 | 0.2857 | 4 | 选项值11, F32, 0 |
| ContentsOptionTable | mOptionDesc12 | 0.2857 | 4 | 选项说明12, CBwString, 采集/制作最大等级限制 |
| ContentsOptionTable | mOptionValue12 | 0.2857 | 4 | 选项值12, F32, 60 |
| ContentsOptionTable | mOptionDesc13 | 0.2857 | 4 | 选项说明13, CBwString, 阵营聊天限制 |
| ContentsOptionTable | mOptionValue13 | 0.2857 | 4 | 选项值13, F32, 6 |
| ContentsOptionTable | mOptionDesc14 | 0.2857 | 4 | 选项说明14, CBwString, 角色删除等待时间值（24小时（每隔一定级别） |
| ContentsOptionTable | mOptionValue14 | 0.2857 | 4 | 选项值14, F32, 24 |
| ContentsOptionTable | mOptionDesc15 | 0.2857 | 4 | 选项说明15, CBwString, 角色恢复期（日） |
| ContentsOptionTable | mOptionValue15 | 0.2857 | 4 | 选项值15, F32, 30 |
| ContentsOptionTable | mOptionDesc16 | 0.2857 | 4 | 选项说明16, CBwString, 角色名称冷却时间（日） |
| ContentsOptionTable | mOptionValue16 | 0.2857 | 4 | 选项值16, F32, 0 |
| ContentsOptionTable | mOptionDesc17 | 0.2143 | 3 | 选项说明17, CBwString, 拍卖场最大登录数 |
| ContentsOptionTable | mOptionValue17 | 0.2143 | 3 | 选项值17, F32, 10 |
| ContentsOptionTable | mOptionDesc18 | 0.1429 | 2 | 选项说明18, CBwString |
| ContentsOptionTable | mOptionValue18 | 0.1429 | 2 | 选项值18, F32 |
| ContentsOptionTable | mOptionDesc19 | 0.1429 | 2 | 选项说明19, CBwString |
| ContentsOptionTable | mOptionValue19 | 0.1429 | 2 | 选项值19, F32 |
| CustomizePreviewTable | TID | 1.0 | 10 | 人物ID, 2, U16 |
| CustomizePreviewTable | Race | 1.0 | 7 | 种族, 0, U8 |
| CustomizePreviewTable | Gen | 1.0 | 5 | 性别, 0, U8 |
| CustomizePreviewTable | BaseEquip_Lance | 0.6364 | 5 | 基础装备 矛, 2, U32:v |
| CustomizePreviewTable | BaseEquip_Staff | 0.6364 | 5 | 基础装备 盾, 2, U32:v |
| CustomizePreviewTable | BaseEquip_Axe | 0.4545 | 5 | 基础装备 斧, 2, U32:v |
| CustomizePreviewTable | BaseEquip_Bow | 0.6364 | 5 | 基础装备 弓, 2, U32:v |
| CustomizePreviewTable | BaseEquip_Charkram | 0.2727 | 3 | 基础装备 能量, 2, U32:v |
| CustomizePreviewTable | BaseEquip_Dagger | 0.2727 | 3 | 基础装备 短剑, 2, U32:v |
| CustomizePreviewTable | BaseEquip_Orb | 0.4545 | 5 | 基础装备 天体, 2, U32:v |
| CustomizePreviewTable | BaseEquip_MagicGun | 0.4545 | 5 | 基础装备 马坦枪, 2, U32:v |
| CustomizePreviewTable | BaseEquip_Sword | 0.6364 | 5 | 基础装备 单手剑, 2, U32:v |
| CustomizePreviewTable | BaseEquip_Wand | 0.6364 | 5 | 基础装备 权杖, 2, U32:v |
| CustomizePreviewTable | BaseEquip_Blade | 0.4545 | 5 | 基础装备 双手剑, 2, U32:v |
| CustomizePreviewTable | BaseEquip_Arbalest | 0.6364 | 5 | 基础装备 石弓, 2, U32:v |
| CustomizePreviewTable | Movie_Lance | 1.0 | 4 | 武器弓动画, 2, CBwString |
| CustomizePreviewTable | Movie_Staff | 1.0 | 4 | 武器盾动画, 2, CBwString |
| CustomizePreviewTable | Movie_Axe | 1.0 | 4 | 武器斧动画, 2, CBwString |
| CustomizePreviewTable | Movie_Bow | 1.0 | 4 | 武器弓动画, 2, CBwString |
| CustomizePreviewTable | Movie_Charkram | 1.0 | 4 | 武器能量动画, 2, CBwString |
| CustomizePreviewTable | Movie_Dagger | 1.0 | 4 | 武器弹弓动画, 2, CBwString |
| CustomizePreviewTable | Movie_Orb | 1.0 | 4 | 武器天体动画, 2, CBwString |
| CustomizePreviewTable | Movie_MagicGun | 1.0 | 4 | 武器马坦枪动画, 2, CBwString |
| CustomizePreviewTable | Movie_Sword | 1.0 | 4 | 武器单手剑动画, 2, CBwString |
| CustomizePreviewTable | Movie_Wand | 1.0 | 4 | 武器权杖动画, 2, CBwString |
| CustomizePreviewTable | Movie_Blade | 1.0 | 4 | 武器双手剑动画, 2, CBwString |
| CustomizePreviewTable | Movie_Arbalest | 1.0 | 4 | 武器石弓动画, 2, CBwString |
| CustomizePreviewTable | EquipView01 | 1.0 | 5 | 装备试穿视角, 2, U32:v |
| CustomizePreviewTable | EquipView02 | 1.0 | 5 | 装备试穿视角2, 2, U32:v |
| CustomizePreviewTable | EquipView03 | 1.0 | 5 | 装备试穿视角3, 2, U32:v |
| CustomizeTable | TID | 1.0 | 3300 | 人物卡斯特帕斯 , 0, U32 |
| CustomizeTable | Type | 1.0 | 8 | 卡斯特部位区分.0=SkinForm. 1=SkinColor. 2=HairForm. 3=HairColor. 4=FaceForm. 5=EyeForm, 0, U32 |
| CustomizeTable | TermsTID | 0.8855 | 367 | 先行部位, 2, U32:v |
| CustomizeTable | Name | 1.0 | 416 | 韩语名, 2, CBwString |
| CustomizeTable | EngName | 0.0009 | 3 | 英文名, 2, CBwString |
| CustomizeTable | Price | 1.0 | 7 | 销售价格, 0, U32 |
| CustomizeTable | bCreate | 1.0 | 4 | 援助方式, 0, U32 |
| CustomizeTable | Icon | 0.9515 | 1377 | 标识, 2, string |
| CustomizeTable | Model | 1.0 | 2802 | 模型, 2, string |
| CustomizeTable | reqPCType | 1.0 | 11 | 种族性别, 0, U32 |
| CustomizeTable | reqItem1 | 0.0009 | 3 | 所需条款, 0, U32 |
| CustomizeTable | reqItemCount1 | 0.0009 | 3 | 所需条款1个数, 0, U32 |
| CustomizeTable | reqItem2 | 0.0009 | 3 | 所需条款2TID, 0, U32 |
| CustomizeTable | reqItemCount2 | 0.0009 | 3 | 所需条款2个数, 0, U32 |
| CustomizeTable | reqItem3 | 0.0009 | 3 | 所需条款3TID, 0, U32 |
| CustomizeTable | reqItemCount3 | 0.0009 | 3 | 所需条款3个数, 0, U32 |
| EffectEventTable | ID | 1.0 | 42 | ID뵀쯤, 2, U32 |
| EffectEventTable | EventName | 1.0 | 43 | 삶땡츰, 2, CBwString |
| EffectEventTable | TargetEvent | 0.2093 | 9 | 朞嶝삶땡ID뵀쯤, 2, U32 |
| EffectEventTable | ReturnEvent | 0.1395 | 4 | 럿쀼삶땡, 2, U32 |
| EntityTable | TID | 0.9987 | 758 | 分隔符, U32, 1 |
| EntityTable | Type | 0.9987 | 3 | 类型, U8, 3 |
| EntityTable | Kind | 0.9987 | 15 | 种类, U8, 8 |
| EntityTable | Property | 0.9987 | 7 | 属性, U8, 0 |
| EntityTable | Race | 0.9987 | 5 | 种族, U8:v, 0 |
| EntityTable | ShapeID | 0.9987 | 114 | 外形信息, U32, 12010 |
| EntityTable | Color | 0.0738 | 17 | RGB 值, string, 160,97,61 |
| EntityTable | Width | 0.9987 | 9 | NPC 大小宽度, F32, 0.3 |
| EntityTable | Height | 0.9987 | 17 | NPC 大小高度, F32, 1.5 |
| EntityTable | Scale | 0.9987 | 14 | NPC 尺寸, F32, 1 |
| EntityTable | Comment | 0.6074 | 283 | 私用, CBwString, 哥布林山地营地 |
| EntityTable | EngTitle | 0.9816 | 745 | 英文标题名称, CBwString, ETT_Title_000001 |
| EntityTable | EngName | 0.9816 | 745 | 英文名称, CBwString, ETT_Name_000001 |
| EntityTable | LocalTitle | 0.1094 | 25 | 本地标题名称, CBwString, 大都市 |
| EntityTable | LocalName | 0.9684 | 699 | 本地名称, CBwString, 哥布林粮食口袋 |
| EntityTable | UseIconType | 0.9987 | 6 | 是否使用图, U8, 1 |
| EntityTable | WorldMapIcon | 0.9987 | 22 | 世界地图上显示的图标, U32, 20800 |
| EntityTable | Level | 0.9987 | 29 | 等级, U8, 1 |
| EntityTable | Repeat | 0.9987 | 7 | 重复采集, U8, 2 |
| EntityTable | ItemDropTID | 0.9987 | 538 | 掉落道具, U16, 20000 |
| EntityTable | RegenR | 0.9987 | 4 | 赞助半径, F32, 0 |
| EntityTable | RegenTimeMin | 0.9987 | 28 | 赞助时间最小, U32, 5 |
| EntityTable | RegenTimeMax | 0.9987 | 28 | 最大赞助时间, U32, 10 |
| EntityTable | Exp | 0.9987 | 43 | 采集物经验值, S64, 0 |
| EntityTable | ActionTID | 0.9987 | 10 | PC行动 ID, U32, 2 |
| EntityTable | Trigger | 0.9987 | 4 | 触发器有/无(0=无.1=有), U8, 0 |
| EntityTable | EntityState | 0.9987 | 4 | 实体状态值(0=idle, 1= 关闭, 2= 打开), U8:v, 0 |
| EntityTable | EntityAni_01 | 0.9987 | 3 | 1#实体号码, U8:a:EntityAni, 0 |
| EntityTable | EntityAni_02 | 0.9987 | 4 | 2#实体号码, U8, 0 |
| EntityTable | EntityAni_03 | 0.9987 | 4 | 3#实体号码, U8, 0 |
| EntityTable | QuestTID | 0.9987 | 473 | 探索 TID, U32, 10014 |
| EntityTable | QuestMissionTID | 0.9987 | 486 | 探索任务 TID, U32, 10014 |
| EntityTable | InsMapGroupTID | 0.9987 | 27 | 可用团队号码, U16, 0 |
| EntityTable | EventRange | 0.9987 | 5 | 事件发生时距离值, U8, 3 |
| EventTable | TID | 0.9643 | 27 | TID, U32, 1 |
| EventTable | SvrNo | 0.9643 | 3 | 服务器号码, U32, 0 |
| EventTable | Type | 0.9643 | 4 | 活动类型, U8, 0 |
| EventTable | World | 0.9643 | 3 | 适用场所, U8, 0 |
| EventTable | Fixed | 0.9643 | 4 | 是否固定, U8, 0 |
| EventTable | Title | 0.9643 | 27 | 标题, CBwString, 经验值 10% 增加 |
| EventTable | NoticeType | 0.9643 | 5 | 有无活动标记, U8, 2 |
| EventTable | DayStart | 0.2143 | 5 | 开始日, CBwString, 2013/11/5 |
| EventTable | DayEnd | 0.2143 | 5 | 结束日, CBwString, 2013/11/6 |
| EventTable | DayWeek | 0.0714 | 2 | 星期, U8 |
| EventTable | TimeStart | 0.1429 | 3 | 开始时间, U32, 6 |
| EventTable | TimeEnd | 0.1429 | 3 | 结束时间, U32, 0 |
| EventTable | Exp | 0.8214 | 13 | 经验值 增加(%), U32, 10 |
| EventTable | WExp | 0.8214 | 13 | 武器熟练度 增加(%), U32, 10 |
| EventTable | GhelldDrop | 0.1071 | 3 | Ghelld 获得量 增加(%), U32, 10 |
| EventTable | Fame | 0.8214 | 4 | 声望 增加(%) : 只作用于全战场 ., U32, 0 |
| EventTable | WarCoinCnt | 0.0714 | 2 | 金币 增加(+), U32 |
| EventTable | MedalCnt | 0.0714 | 2 | 勋章 增加(+), U32 |
| EventTable | AddSkill | 0.0714 | 2 | 技能适用 SkillTable创造, U32:v |
| EventTable | ItemDropRate | 0.8214 | 13 | 掉率增加项目(%), U32, 0 |
| EventTable | DropItem | 0.0714 | 2 | 掉率增加项目(ItemDropWorldTable 创造), U32:v |
| EventTable | GiftType | 0.9643 | 5 | 礼物类型, U8, 0 |
| EventTable | GiftTerm | 0.1429 | 4 | 礼物时间间隔, U8, 1 |
| EventTable | GiftCheck | 0.2143 | 4 | 礼物格子数量是否增加, U8, 1 |
| EventTable | GiftMail | 0.2143 | 6 | 邮寄礼物 TID, U32:v, 2002 |
| FamePointTable | TID | 0.9565 | 22 | 索引, U8, 1 |
| FamePointTable | EngAimName | 0.9565 | 22 | 英文标题名, CBwString, FPT_Aim_000001 |
| FamePointTable | EngDemolName | 0.9565 | 22 | 英文标题名, CBwString, FPT_Demol_000001 |
| FamePointTable | LocalAimName | 0.9565 | 22 | 阶层, CBwString, 10级 战士 |
| FamePointTable | LocalDemolName | 0.9565 | 22 | 阶层, CBwString, 10级 战士 |
| FamePointTable | ReqPoint | 0.9565 | 22 | 需要声望点数, U32, 0 |
| FamePointTable | TotalPoint | 0.9565 | 22 | 声望点总和, U32, 0 |
| FixedDummyAniTable | TID | 1.0 | 55 | 煦燭, 2, U16 |
| FixedDummyAniTable | AniID | 0.9821 | 55 | 雄賒ID, U32, 8003 |
| GuildTable | TID | 0.9231 | 12 | 工会等级, U8, 1 |
| GuildTable | ReqPerson | 0.9231 | 12 | 所需人员数, U8, 0 |
| GuildTable | ReqExp | 0.9231 | 12 | 所需经验值, U32, 0 |
| GuildTable | ReqMoney | 0.9231 | 12 | 所需工会资金, U32, 0 |
| GuildTable | Tax | 0.9231 | 12 | 工会税金, U32, 1000 |
| GuildTable | Slot | 0.9231 | 7 | 公会仓库插槽, U8, 20 |
| GuildTable | Name | 0.9231 | 11 | 授予称谓个数, U8, 2 |
| GuildTable | Person | 0.9231 | 12 | 公会人数, U8, 10 |
| GuildTable | GuildSkill | 0.8462 | 11 | 公会技能, U32:v, 230251|230261 |
| HelpTable | TID | 1.0 | 34 | 分离器, 2, U16 |
| HelpTable | Comment | 1.0 | 35 | 企划者用, 2, CBwString |
| HelpTable | EngTitle | 1.0 | 35 | 英文类型名, 2, CBwString |
| HelpTable | LocalTitle | 1.0 | 11 | 韩文类型名, 2, CBwString |
| HelpTable | EngName | 1.0 | 35 | 英文种类名, 2, CBwString |
| HelpTable | LocalName | 1.0 | 35 | 韩文种类名, 2, CBwString |
| HelpTable | Type | 1.0 | 11 | 类型, 2, U8 |
| HelpTable | Kind | 1.0 | 8 | 种类, 2, U8 |
| HelpTable | EngDesc | 1.0 | 35 | 英文说明, 2, CBwString |
| HelpTable | LocalDesc | 1.0 | 35 | 韩文说明, 2, CBwString |
| InstanceMapTable | TID | 0.9917 | 119 | 当前可用地图号, U16, 4000 |
| InstanceMapTable | GroupTID | 0.9917 | 32 | 小队号, U16, 1 |
| InstanceMapTable | Difficulty | 0.9917 | 6 | 难易度, U8, 1 |
| InstanceMapTable | Comment | 0.9833 | 12 | 企划者用, CBwString, 普通 |
| InstanceMapTable | EngName | 0.9917 | 119 | 当前可用英文名, CBwString, IMT_Name_000001 |
| InstanceMapTable | LocalName | 0.9917 | 28 | 当前可用韩文名, CBwString, 洛坎的实验室 |
| InstanceMapTable | Goal | 0.9917 | 119 | 目标, U32:v, 1 |
| InstanceMapTable | LimitTime | 0.9917 | 9 | 时间限制, U32, 1800000 |
| InstanceMapTable | ReqJoinType | 0.9917 | 4 | 可能入场条件, U8, 0 |
| InstanceMapTable | MinPerson | 0.9917 | 3 | 最小人数, U8, 1 |
| InstanceMapTable | MaxPerson | 0.9917 | 5 | 最大人数, U8, 2 |
| InstanceMapTable | ReqPerson | 0.9917 | 7 | 人员奖励, CBwString, 1~2 |
| InstanceMapTable | ReqMinLevel | 0.9917 | 16 | 最少需要的电脑等级, U8, 10 |
| InstanceMapTable | ReqMaxLevel | 0.9917 | 5 | 最大需要的电脑等级, U8, 50 |
| InstanceMapTable | ReqItem | 0.9917 | 5 | 需要物品, U32, 0 |
| InstanceMapTable | ReqItem_Count | 0.9917 | 4 | 需要物品数量, U8, 0 |
| InstanceMapTable | GoalPoint | 0.9917 | 62 | 目标分数, U32, 21247 |
| InstanceMapTable | GoalPoint_SSS_TID | 0.9917 | 84 | SSS任务分数奖励 TID, U16:v, 1010|1040|1010|1040 |
| InstanceMapTable | GoalPoint_SS_TID | 0.9917 | 84 | SS任务分数奖励 TID, U16:v, 1011|1041|1011|1041 |
| InstanceMapTable | GoalPoint_S_TID | 0.9917 | 84 | S任务分数奖励 TID, U16:v, 1012|1042|1012|1042 |
| InstanceMapTable | GoalPoint_A_TID | 0.9917 | 84 | A任务分数奖励 TID, U16:v, 1013|1043|1013|1043 |
| InstanceMapTable | GoalPoint_B_TID | 0.9917 | 84 | B任务分数奖励 TID, U16:v, 1014|1044|1014|1044 |
| InstanceMapTable | GoalPoint_F_TID | 0.9917 | 83 | C任务分数奖励 TID, U16:v, 1015|1045|1015|1045 |
| InstanceMapTable | Img | 0.9917 | 22 | 原画形象, U16, 1 |
| InstanceMapTable | Matching | 0.9917 | 4 | 组队注册 有/无, U8, 1 |
| InstanceMapTable | ShowDifficulty | 0.9917 | 4 | 入场 UI 有无难易度按键标记(控制是否公开), U8, 1 |
| InstanceMapTable | RolePerson | 0.9917 | 5 | 角色名额(按坦克.治疗.输出顺序), U8:v, 1|1|1 |
| InstanceMapTable | EngDesc | 0.9917 | 119 | 英文说明, CBwString, IMT_Desc_000001 |
| InstanceMapTable | LocalDesc | 0.9917 | 4 | 韩文说明, CBwString, 干掉所有目标怪物 |
| InstanceRewardTable | TID | 0.999 | 962 | ЗжРыЦї, U16, 1010 |
| InstanceRewardTable | RewardTID | 0.999 | 82 | МДЪБЕиЭМВЮПМTID TID КХТы, U16, 4000 |
| InstanceRewardTable | Comment | 0.999 | 962 | ЦѓЛЎепгУ(ПЩгУВЙГЅКЭЕиЭМУћГЦ), CBwString, ТхПВЕФЪЕбщЪв (ШЫРр, ЦеЭЈ)-SSS НБРј |
| InstanceRewardTable | BoxColor | 0.999 | 6 | БІЮяЯфзгбеЩЋ, U8, 5 |
| InstanceRewardTable | RewardItem01 | 0.999 | 47 | 01#НБРјЮяЦЗ, U32, 81000 |
| InstanceRewardTable | RewardItemStack01 | 0.999 | 4 | 01#НБРјЮяЦЗжиКЯЪ§СП, U8, 1 |
| InstanceRewardTable | RewardRate01 | 0.999 | 30 | 01#НБРјИХТЪ, U16, 925 |
| InstanceRewardTable | RewardItem02 | 0.999 | 95 | 2#НБРјЮяЦЗ, U32, 81001 |
| InstanceRewardTable | RewardItemStack02 | 0.999 | 9 | 02#НБРјЮяЦЗжиКЯЪ§СП, U8, 1 |
| InstanceRewardTable | RewardRate02 | 0.999 | 47 | 2#НБРјИХТЪ, U16, 4625 |
| InstanceRewardTable | RewardItem03 | 0.999 | 92 | 3#НБРјЮяЦЗ, U32, 81002 |
| InstanceRewardTable | RewardItemStack03 | 0.999 | 9 | 03#НБРјЮяЦЗжиКЯЪ§СП, U8, 1 |
| InstanceRewardTable | RewardRate03 | 0.999 | 46 | 3#НБРјИХТЪ, U16, 9250 |
| InstanceRewardTable | RewardItem04 | 0.999 | 92 | 4#НБРјЮяЦЗ, U32, 2080011 |
| InstanceRewardTable | RewardItemStack04 | 0.999 | 9 | 04#НБРјЮяЦЗжиКЯЪ§СП, U8, 1 |
| InstanceRewardTable | RewardRate04 | 0.999 | 47 | 4#НБРјИХТЪ, U16, 9288 |
| InstanceRewardTable | RewardItem05 | 0.9242 | 88 | 5#НБРјЮяЦЗ, U32, 2080012 |
| InstanceRewardTable | RewardItemStack05 | 0.9242 | 9 | 05#НБРјЮяЦЗжиКЯЪ§СП, U8, 1 |
| InstanceRewardTable | RewardRate05 | 0.9242 | 42 | 5#НБРјИХТЪ, U16, 9326 |
| InstanceRewardTable | RewardItem06 | 0.7622 | 83 | 06#НБРјЮяЦЗ, U32, 2080021 |
| InstanceRewardTable | RewardItemStack06 | 0.7622 | 4 | 06#НБРјЮяЦЗжиКЯЪ§СП, U8, 1 |
| InstanceRewardTable | RewardRate06 | 0.7622 | 41 | 06#НБРјИХТЪ, U16, 9476 |
| InstanceRewardTable | RewardItem07 | 0.7373 | 88 | 07#НБРјЮяЦЗ, U32, 2080022 |
| InstanceRewardTable | RewardItemStack07 | 0.7373 | 4 | 07#НБРјЮяЦЗжиКЯЪ§СП, U8, 1 |
| InstanceRewardTable | RewardRate07 | 0.7373 | 30 | 07#НБРјИХТЪ, U16, 9626 |
| InstanceRewardTable | RewardItem08 | 0.7082 | 54 | 08#НБРјЮяЦЗ, U32, 2080031 |
| InstanceRewardTable | RewardItemStack08 | 0.7082 | 5 | 08#НБРјЮяЦЗжиКЯЪ§СП, U8, 1 |
| InstanceRewardTable | RewardRate08 | 0.7082 | 19 | 08#НБРјИХТЪ, U16, 9814 |
| InstanceRewardTable | RewardItem09 | 0.6584 | 35 | 09#НБРјЮяЦЗ, U32, 2080032 |
| InstanceRewardTable | RewardItemStack09 | 0.6584 | 5 | 09#НБРјЮяЦЗжиКЯЪ§СП, U8, 1 |
| InstanceRewardTable | RewardRate09 | 0.6584 | 9 | 09#НБРјИХТЪ, U16, 10000 |
| InstanceRewardTable | RewardItem10 | 0.5504 | 9 | 10#НБРјЮяЦЗ, U32, 0 |
| InstanceRewardTable | RewardItemStack10 | 0.5504 | 5 | 10#НБРјЮяЦЗжиКЯЪ§СП, U8, 0 |
| InstanceRewardTable | RewardRate10 | 0.5504 | 4 | 10#НБРјИХТЪ, U16, 0 |
| InstanceRoundTable | TID | 0.9924 | 130 | 分离器, U16, 1 |
| InstanceRoundTable | Comment | 0.0611 | 8 | 企划者用, CBwString, Lv.5 ?? ?? |
| InstanceRoundTable | EngDesc | 0.9924 | 130 | 英文目标说明, CBwString, IRT_Desc_000001 |
| InstanceRoundTable | LocalDesc | 0.9924 | 114 | 韩文目标说明, CBwString, 洛坎的实验室 (普通) |
| InstanceRoundTable | Type | 0.9924 | 4 | 所有, U8, 2 |
| InstanceRoundTable | Round | 0.9924 | 14 | 副本号码, U8, 1 |
| InstanceRoundTable | RoundTime | 0.9924 | 9 | 副本时间限制, U32, 1800000 |
| InstanceRoundTable | RoundWaitTime | 0.9924 | 4 | 副本开始等候时间, U32, 0 |
| InstanceRoundTable | AutoRound | 0.9924 | 4 | 限制时间过后副本自动生成 有/无, U8, 0 |
| InstanceRoundTable | NpcTID | 0.9924 | 100 | 怪物 TID 号码, U32:v, 150005|150008 |
| InstanceRoundTable | NpcCount | 0.9924 | 16 | 目标怪物数量, U8:v, 1|1 |
| Interpolator | ID | 0.9884 | 84 | 2, CBwString, #DayLight Ambient Color |
| Interpolator | Content | 0.9884 | 4 | 2, U8, 1 |
| Interpolator | Type | 0.9884 | 2 | 2, U8 |
| Interpolator | MaxTime | 0.9884 | 11 | 2, F32, 24 |
| Interpolator | Data | 0.9884 | 83 | 2, CBwString, 0.00000|50.19608|0.00000|100.00000|0.00000|0.00000|0.00000|0.00000|0.00000|0.00000|-150.58824|0.00000|-300.00000|100.39216|0.00000|200.00000|24.00000|0.00000|0.00000|0.00000|0.00000|0.00000|0.00000|0.00000|0.00000|0.00000|0.00000|0.00000|0.00000|0.00000|0.00000|0.00000| |
| ItemAlchemyTable | TID | 0.9524 | 20 | 区分号码, U32, 1 |
| ItemAlchemyTable | Comment | 0.9048 | 19 | CBwString, 最低级精灵石炼成术(武器用), 低级精灵石炼成术(武器用) |
| ItemAlchemyTable | CostGhelld | 0.9524 | 8 | 企划者用, U32, 50 |
| ItemAlchemyTable | ItemTID | 0.9524 | 20 | 媒介物品, U32, 41000 |
| ItemAlchemyTable | MaxMaterial | 0.9524 | 3 | 材料最大个数, U16, 50 |
| ItemAlchemyTable | Item01TID | 0.9524 | 20 | 成品价格, U32, 51200 |
| ItemAlchemyTable | Item01Stack | 0.9524 | 3 | 重合, U16, 1 |
| ItemAlchemyTable | Item01Rate | 0.9524 | 10 | 被选中概率, U16, 120 |
| ItemAlchemyTable | Item02TID | 0.9524 | 20 | 成品价格, U32, 51000 |
| ItemAlchemyTable | Item02Stack | 0.9524 | 3 | 重合, U16, 1 |
| ItemAlchemyTable | Item02Rate | 0.9524 | 16 | 被选中概率, U16, 420 |
| ItemAlchemyTable | Item03TID | 0.9524 | 20 | 成品价格, U32, 51100 |
| ItemAlchemyTable | Item03Stack | 0.9524 | 3 | 重合, U16, 1 |
| ItemAlchemyTable | Item03Rate | 0.9524 | 17 | 被选中概率, U16, 900 |
| ItemAlchemyTable | Item04TID | 0.9524 | 20 | 成品价格, U32, 51050 |
| ItemAlchemyTable | Item04Stack | 0.9524 | 3 | 重合, U16, 1 |
| ItemAlchemyTable | Item04Rate | 0.9524 | 10 | 被选中概率, U16, 1800 |
| ItemAlchemyTable | Item05TID | 0.9524 | 20 | 成品价格, U32, 51150 |
| ItemAlchemyTable | Item05Stack | 0.9524 | 3 | 重合, U16, 1 |
| ItemAlchemyTable | Item05Rate | 0.9524 | 15 | 被选中概率, U16, 3600 |
| ItemAlchemyTable | Item06TID | 0.9524 | 15 | 成品价格, U32, 51250 |
| ItemAlchemyTable | Item06Stack | 0.9524 | 3 | 重合, U16, 1 |
| ItemAlchemyTable | Item06Rate | 0.9524 | 13 | 被选中概率, U16, 6000 |
| ItemAlchemyTable | Item07TID | 0.6667 | 9 | 成品价格, U32, 37000 |
| ItemAlchemyTable | Item07Stack | 0.9524 | 4 | 重合, U16, 1 |
| ItemAlchemyTable | Item07Rate | 0.9524 | 9 | 被选中概率, U16, 10000 |
| ItemAlchemyTable | Item08TID | 0.9524 | 4 | 成品价格, U32, 0 |
| ItemAlchemyTable | Item08Stack | 0.9524 | 4 | 重合, U16, 0 |
| ItemAlchemyTable | Item08Rate | 0.9524 | 4 | 被选中概率, U16, 0 |
| ItemAlchemyTable | Item09TID | 0.9524 | 3 | 成品价格, U32, 0 |
| ItemAlchemyTable | Item09Stack | 0.9524 | 3 | 重合, U16, 0 |
| ItemAlchemyTable | Item09Rate | 0.9524 | 3 | 被选中概率, U16, 0 |
| ItemAlchemyTable | Item10TID | 0.9524 | 3 | 成品价格, U32, 0 |
| ItemAlchemyTable | Item10Stack | 0.9524 | 3 | 重合, U16, 0 |
| ItemAlchemyTable | Item10Rate | 0.9524 | 3 | 被选中概率, U16, 0 |
| ItemBoxTable | TID | 0.9992 | 1288 | 箱子TID, U16, 1 |
| ItemBoxTable | Comment | 0.9992 | 1250 | 规划者用（物品名称填写）, CBwString, 高级 Lv.30 武器 箱子 |
| ItemBoxTable | Group | 0.9992 | 305 | 团队箱子(Item桌面 BoxTID 引用), U16, 1 |
| ItemBoxTable | GroupRate | 0.9992 | 47 | 团队特别的下降概率, U16, 10000 |
| ItemBoxTable | BoxItem01 | 0.9992 | 1156 | 01#箱子道具, U32, 1021621 |
| ItemBoxTable | BoxItemStack01 | 0.9992 | 11 | 01#重叠量, U8, 1 |
| ItemBoxTable | DropRate01 | 0.9992 | 25 | 01#下降率, U16, 10000 |
| ItemBoxTable | BoxItem02 | 0.9992 | 1161 | 2#箱子道具, U32, 1031621 |
| ItemBoxTable | BoxItemStack02 | 0.9992 | 11 | 2#重叠量, U8, 1 |
| ItemBoxTable | DropRate02 | 0.9992 | 32 | 2#下降率, U16, 10000 |
| ItemBoxTable | BoxItem03 | 0.8619 | 1039 | 3#箱子道具, U32, 1111621 |
| ItemBoxTable | BoxItemStack03 | 0.8619 | 10 | 3#重叠量, U8, 1 |
| ItemBoxTable | DropRate03 | 0.8619 | 32 | 3#下降量, U16, 10000 |
| ItemBoxTable | BoxItem04 | 0.8518 | 1022 | 4#箱子道具, U32, 1121621 |
| ItemBoxTable | BoxItemStack04 | 0.8518 | 11 | 4#重叠量, U8, 1 |
| ItemBoxTable | DropRate04 | 0.8518 | 31 | 4#下降量, U16, 10000 |
| ItemBoxTable | BoxItem05 | 0.5454 | 664 | 5#箱子道具, U32, 1131621 |
| ItemBoxTable | BoxItemStack05 | 0.5454 | 11 | 5#重叠量, U8, 1 |
| ItemBoxTable | DropRate05 | 0.5454 | 30 | 5#下降量, U16, 10000 |
| ItemBoxTable | BoxItem06 | 0.5105 | 619 | 6#箱子道具, U32, 110500 |
| ItemBoxTable | BoxItemStack06 | 0.5105 | 9 | 6#重叠量, U8, 1 |
| ItemBoxTable | DropRate06 | 0.5105 | 24 | 6#下降量, U16, 10000 |
| ItemBoxTable | BoxItem07 | 0.0644 | 62 | 7#箱子道具, U32, 110501 |
| ItemBoxTable | BoxItemStack07 | 0.0644 | 11 | 7#重叠量, U8, 1 |
| ItemBoxTable | DropRate07 | 0.0644 | 21 | 7#下降量, U16, 10000 |
| ItemBoxTable | BoxItem08 | 0.0489 | 42 | 8#箱子道具, U32, 115500 |
| ItemBoxTable | BoxItemStack08 | 0.0489 | 9 | 8#重叠量, U8, 1 |
| ItemBoxTable | DropRate08 | 0.0489 | 14 | 8#下降量, U16, 10000 |
| ItemBoxTable | BoxItem09 | 0.0287 | 27 | 9#箱子道具, U32, 115501 |
| ItemBoxTable | BoxItemStack09 | 0.0287 | 7 | 9#重叠量, U8, 1 |
| ItemBoxTable | DropRate09 | 0.0287 | 8 | 9#下降量, U16, 10000 |
| ItemBoxTable | BoxItem10 | 0.0194 | 16 | 10#箱子道具, U32, 2160921 |
| ItemBoxTable | BoxItemStack10 | 0.0194 | 4 | 10#重叠量, U8, 1 |
| ItemBoxTable | DropRate10 | 0.0194 | 4 | 10#下降量, U16, 10000 |
| ItemBreakTable | TID | 0.9969 | 322 | BreakTID 参考, U32, 101 |
| ItemBreakTable | Comment | 0.9969 | 322 | 企划者用(项目名拟定), CBwString, 武器_01~10_一般 |
| ItemBreakTable | AddBreakNumber | 0.9969 | 5 | 进一步分解次数, U8, 0 |
| ItemBreakTable | AddBreakRate | 0.9969 | 6 | 进一步分解概率, U16, 0 |
| ItemBreakTable | BreakItem01 | 0.9969 | 20 | 01#分解物品, U32, 40000 |
| ItemBreakTable | BreakItemStack01 | 0.9969 | 3 | 01#分解物品重合数量, U8, 1 |
| ItemBreakTable | BreakRate01 | 0.9969 | 6 | 01#分解概率, U16, 10 |
| ItemBreakTable | BreakItem02 | 0.9969 | 7 | 2#分解物品, U32, 40600 |
| ItemBreakTable | BreakItemStack02 | 0.9969 | 3 | 2#分解物品重合数量, U8, 1 |
| ItemBreakTable | BreakRate02 | 0.9969 | 6 | 2#分解概率, U16, 3010 |
| ItemBreakTable | BreakItem03 | 0.9969 | 3 | 3#分解物品, U32, 37000 |
| ItemBreakTable | BreakItemStack03 | 0.9969 | 3 | 3#分解物品重合数量, U8, 1 |
| ItemBreakTable | BreakRate03 | 0.9969 | 3 | 3#分解概率, U16, 10000 |
| ItemBreakTable | FGambleGhelld | 0.9969 | 20 | 2次下注所需手续费, U32, 6 |
| ItemBreakTable | FGambleItem01 | 0.9969 | 20 | 01#风险分解物品, U32, 40000 |
| ItemBreakTable | FGambleItemStack01 | 0.9969 | 3 | 01#下注物品重合数量, U8, 1 |
| ItemBreakTable | FGambleRate01 | 0.9969 | 6 | 01#下注物品概率, U16, 50 |
| ItemBreakTable | FGambleItem02 | 0.9969 | 7 | 2#下注分解物品, U32, 40600 |
| ItemBreakTable | FGambleItemStack02 | 0.9969 | 4 | 2#下注物品重合数量, U8, 1 |
| ItemBreakTable | FGambleRate02 | 0.9969 | 5 | 2#下注物品概率, U16, 9000 |
| ItemBreakTable | FGambleItem03 | 0.9969 | 8 | 3#下注分解物品, U32, 37000 |
| ItemBreakTable | FGambleItemStack03 | 0.9969 | 4 | 3#下注物品重合数量, U8, 1 |
| ItemBreakTable | FGambleRate03 | 0.9969 | 3 | 3#下注物品概率, U16, 10000 |
| ItemBreakTable | SGambleGhelld | 0.9969 | 20 | 3次所需手续费, U32, 12 |
| ItemBreakTable | SGambleItem01 | 0.9969 | 20 | 1#下注分解物品, U32, 40000 |
| ItemBreakTable | SGambleItemStack01 | 0.9969 | 3 | 1#下注物品重合数量, U8, 1 |
| ItemBreakTable | SGambleRate01 | 0.9969 | 6 | 1#下注物品概率, U16, 140 |
| ItemBreakTable | SGambleItem02 | 0.9969 | 13 | 2#下注分解物品, U32, 40600 |
| ItemBreakTable | SGambleItemStack02 | 0.9969 | 6 | 2#下注物品重合数量, U8, 2 |
| ItemBreakTable | SGambleRate02 | 0.9969 | 5 | 2#下注物品概率, U16, 10000 |
| ItemBreakTable | SGambleItem03 | 0.9969 | 10 | 3#下注分解物品, U32, 0 |
| ItemBreakTable | SGambleItemStack03 | 0.9969 | 7 | 3#下注物品重合数量, U8, 0 |
| ItemBreakTable | SGambleRate03 | 0.9969 | 4 | 3#下注物品概率, U16, 0 |
| ItemCoinTable | TID | 0.9091 | 10 | 分离器, U8, 1 |
| ItemCoinTable | Comment | 0.9091 | 8 | 企划者用, CBwString, 药水,熟练度,选择券,小规模券, 尖晶石,分身(人类) |
| ItemCoinTable | EngName | 0.1818 | 2 | 英文物品名, CBwString |
| ItemCoinTable | LocalName | 0.9091 | 6 | 韩文物品名, CBwString, 1级 物品 |
| ItemCoinTable | Type | 0.9091 | 6 | 等级, U8, 1 |
| ItemCoinTable | Race | 0.9091 | 4 | 种族, U8:v, 1 |
| ItemCoinTable | Coin | 0.9091 | 6 | 需要兽人个数, U8, 1 |
| ItemCoinTable | DropItem01 | 0.9091 | 3 | 01#物品掉落, U32, 10016 |
| ItemCoinTable | DropItemStack01 | 0.9091 | 6 | 01#掉落物品重合数量, U8, 2 |
| ItemCoinTable | DropRate01 | 0.9091 | 6 | 01#掉落概率, U16, 1800 |
| ItemCoinTable | DropItem02 | 0.9091 | 3 | 2#掉落物品, U32, 10017 |
| ItemCoinTable | DropItemStack02 | 0.9091 | 6 | 02#掉落物品重合数量, U8, 2 |
| ItemCoinTable | DropRate02 | 0.9091 | 6 | 2#掉落概率, U16, 3600 |
| ItemCoinTable | DropItem03 | 0.9091 | 3 | 3#掉落物品, U32, 10116 |
| ItemCoinTable | DropItemStack03 | 0.9091 | 6 | 03#掉落物品重合数量, U8, 2 |
| ItemCoinTable | DropRate03 | 0.9091 | 6 | 3#掉落概率, U16, 5400 |
| ItemCoinTable | DropItem04 | 0.9091 | 3 | 4#掉落物品, U32, 10117 |
| ItemCoinTable | DropItemStack04 | 0.9091 | 6 | 04#掉落物品重合数量, U8, 2 |
| ItemCoinTable | DropRate04 | 0.9091 | 6 | 4#掉落概率, U16, 7200 |
| ItemCoinTable | DropItem05 | 0.9091 | 3 | 5#掉落物品, U32, 40301 |
| ItemCoinTable | DropItemStack05 | 0.9091 | 3 | 05#掉落物品重合数量, U8, 1 |
| ItemCoinTable | DropRate05 | 0.9091 | 6 | 5#掉落概率, U16, 9000 |
| ItemCoinTable | DropItem06 | 0.9091 | 3 | 6#掉落物品, U32, 9076 |
| ItemCoinTable | DropItemStack06 | 0.9091 | 3 | 06#掉落物品重合数量, U8, 1 |
| ItemCoinTable | DropRate06 | 0.9091 | 6 | 6#掉落概率, U16, 9300 |
| ItemCoinTable | DropItem07 | 0.9091 | 3 | 7#掉落物品, U32, 90062 |
| ItemCoinTable | DropItemStack07 | 0.9091 | 3 | 07#掉落物品重合数量, U8, 1 |
| ItemCoinTable | DropRate07 | 0.9091 | 6 | 7#掉落概率, U16, 9500 |
| ItemCoinTable | DropItem08 | 0.9091 | 3 | 8#掉落物品, U32, 510000 |
| ItemCoinTable | DropItemStack08 | 0.9091 | 3 | 08#掉落物品重合数量, U8, 1 |
| ItemCoinTable | DropRate08 | 0.9091 | 6 | 8#掉落概率, U16, 9650 |
| ItemCoinTable | DropItem09 | 0.9091 | 3 | 9#掉落物品, U32, 40302 |
| ItemCoinTable | DropItemStack09 | 0.9091 | 3 | 09#掉落物品重合数量, U8, 1 |
| ItemCoinTable | DropRate09 | 0.9091 | 6 | 9#掉落概率, U16, 9800 |
| ItemCoinTable | DropItem10 | 0.9091 | 3 | 10#掉落物品, U32, 400001 |
| ItemCoinTable | DropItemStack10 | 0.9091 | 3 | 10#掉落物品重合数量, U8, 1 |
| ItemCoinTable | DropRate10 | 0.9091 | 6 | 10#掉落概率, U16, 9900 |
| ItemCoinTable | DropItem11 | 0.9091 | 4 | 11#掉落物品, U32, 400403 |
| ItemCoinTable | DropItemStack11 | 0.9091 | 3 | 11#掉落物品重合数量, U8, 1 |
| ItemCoinTable | DropRate11 | 0.9091 | 6 | 11#掉落概率, U16, 9970 |
| ItemCoinTable | DropItem12 | 0.9091 | 3 | 12#掉落物品, U32, 400400 |
| ItemCoinTable | DropItemStack12 | 0.9091 | 3 | 12#掉落物品重合数量, U8, 1 |
| ItemCoinTable | DropRate12 | 0.9091 | 6 | 12#掉落概率, U16, 9990 |
| ItemCoinTable | DropItem13 | 0.9091 | 3 | 13#掉落物品, U32, 9071 |
| ItemCoinTable | DropItemStack13 | 0.9091 | 3 | 13#掉落物品重合数量, U8, 1 |
| ItemCoinTable | DropRate13 | 0.9091 | 6 | 13#掉落概率, U16, 9995 |
| ItemCoinTable | DropItem14 | 0.9091 | 3 | 14#掉落物品, U32, 40303 |
| ItemCoinTable | DropItemStack14 | 0.9091 | 3 | 14#掉落物品重合数量, U8, 1 |
| ItemCoinTable | DropRate14 | 0.9091 | 3 | 14#掉落概率, U16, 10000 |
| ItemCoinTable | DropItem15 | 0.1818 | 2 | 15#掉落物品, U32 |
| ItemCoinTable | DropItemStack15 | 0.1818 | 2 | 15#掉落物品重合数量, U8 |
| ItemCoinTable | DropRate15 | 0.1818 | 2 | 15#掉落概率, U16 |
| ItemDropLimitTable | TID | 0.75 | 3 | 롸잼포, U16, 1 |
| ItemDropLimitTable | Comment | 0.75 | 3 | 폐뺍諒痰, CBwString, 샨랄돨평摩며꼈주 |
| ItemDropLimitTable | Svr | 0.5 | 2 | 륩蛟포뵀, U8 |
| ItemDropLimitTable | ItemTID | 0.75 | 3 | 되쩍뵀쯤, U32, 2150200 |
| ItemDropLimitTable | ItemStack | 0.75 | 3 | 離댕係운鑒좆, U16, 5 |
| ItemDropTable | TID | 0.9998 | 8731 | U16, 1, 2 |
| ItemDropTable | Comment | 0.9999 | 4891 | 企划者用(怪物名拟写), CBwString, (目标)一般_靴子_1 |
| ItemDropTable | GroupID | 0.9999 | 1476 | 团队号, U32, 1 |
| ItemDropTable | GroupRate | 0.9999 | 1437 | 团队概率, U16, 302 |
| ItemDropTable | MinGhelld | 0.9999 | 508 | 最小Ghelld量, U32, 1 |
| ItemDropTable | MaxGhelld | 0.9999 | 580 | 最大Ghelld量, U32, 1 |
| ItemDropTable | AddDropNumber | 0.9999 | 5 | 追加团队次数, U8, 1 |
| ItemDropTable | AddDropRate | 0.9999 | 1249 | 追加团队概率, U16, 392 |
| ItemDropTable | DropItem01 | 0.9946 | 1536 | 01#物品掉落, U32, 2150001 |
| ItemDropTable | DropItemStack01 | 0.9998 | 7 | 01#物品掉落重合数量, U8, 1 |
| ItemDropTable | DropRate01 | 0.9998 | 17 | 01#掉率, U16, 3333 |
| ItemDropTable | DropItem02 | 0.8553 | 1035 | 2#物品掉落, U32, 2153001 |
| ItemDropTable | DropItemStack02 | 0.8554 | 5 | 02#物品掉落重合数量, U8, 1 |
| ItemDropTable | DropRate02 | 0.8554 | 17 | 2#掉率, U16, 6666 |
| ItemDropTable | DropItem03 | 0.7651 | 788 | 3#物品掉落, U32, 2156001 |
| ItemDropTable | DropItemStack03 | 0.7661 | 4 | 03#物品掉落重合数量, U8, 1 |
| ItemDropTable | DropRate03 | 0.7651 | 12 | 3#掉率, U16, 10000 |
| ItemDropTable | DropItem04 | 0.4373 | 585 | 4#物品掉落, U32, 1130001 |
| ItemDropTable | DropItemStack04 | 0.4373 | 4 | 04#物品掉落重合数量, U8, 1 |
| ItemDropTable | DropRate04 | 0.4373 | 13 | 4#掉率, U16, 10000 |
| ItemDropTable | DropItem05 | 0.4351 | 585 | 5#物品掉落, U32, 1100001 |
| ItemDropTable | DropItemStack05 | 0.4351 | 4 | 05#物品掉落重合数量, U8, 1 |
| ItemDropTable | DropRate05 | 0.4351 | 10 | 5#掉率, U16, 10000 |
| ItemDropTable | DropItem06 | 0.3064 | 521 | 6#物品掉落, U32, 2156011 |
| ItemDropTable | DropItemStack06 | 0.3064 | 4 | 06#物品掉落重合数量, U8, 1 |
| ItemDropTable | DropRate06 | 0.3064 | 10 | 6#掉率, U16, 10000 |
| ItemDropTable | DropItem07 | 0.1209 | 137 | 7#物品掉落, U32, 1120011 |
| ItemDropTable | DropItemStack07 | 0.1209 | 4 | 07#物品掉落重合数量, U8, 1 |
| ItemDropTable | DropRate07 | 0.1209 | 9 | 7#掉率, U16, 7000 |
| ItemDropTable | DropItem08 | 0.0658 | 130 | 8#物品掉落, U32, 1130011 |
| ItemDropTable | DropItemStack08 | 0.0658 | 4 | 08#物品掉落重合数量, U8, 1 |
| ItemDropTable | DropRate08 | 0.0658 | 8 | 8#掉率, U16, 8000 |
| ItemDropTable | DropItem09 | 0.0657 | 129 | 9#物品掉落, U32, 1100011 |
| ItemDropTable | DropItemStack09 | 0.0657 | 3 | 09#物品掉落重合数量, U8, 1 |
| ItemDropTable | DropRate09 | 0.0657 | 7 | 9#掉率, U16, 9000 |
| ItemDropTable | DropItem10 | 0.0646 | 120 | 10#物品掉落, U32, 1100014 |
| ItemDropTable | DropItemStack10 | 0.0646 | 3 | 10#物品掉落重合数量, U8, 1 |
| ItemDropTable | DropRate10 | 0.0646 | 4 | 10#掉率, U16, 10000 |
| ItemDropTable | DropItem11 | 0.0243 | 8 | 11#物品掉落, U32, 60737 |
| ItemDropTable | DropItemStack11 | 0.0243 | 3 | 11#物品掉落重合数量, U8, 1 |
| ItemDropTable | DropRate11 | 0.0243 | 3 | 11#掉率, U16, 10000 |
| ItemDropTable | DropItem12 | 0.0002 | 2 | 12#物品掉落, U32 |
| ItemDropTable | DropItemStack12 | 0.0002 | 2 | 12#物品掉落重合数量, U8 |
| ItemDropTable | DropRate12 | 0.0002 | 2 | 12#掉率, U16 |
| ItemDropTable | DropItem13 | 0.0002 | 2 | 13#物品掉落, U32 |
| ItemDropTable | DropItemStack13 | 0.0002 | 2 | 13#物品掉落重合数量, U8 |
| ItemDropTable | DropRate13 | 0.0002 | 2 | 13#掉率, U16 |
| ItemDropTable | DropItem14 | 0.0002 | 2 | 14#物品掉落, U32 |
| ItemDropTable | DropItemStack14 | 0.0002 | 2 | 14#物品掉落重合数量, U8 |
| ItemDropTable | DropRate14 | 0.0002 | 2 | 14#掉率, U16 |
| ItemDropTable | DropItem15 | 0.0002 | 2 | 15#物品掉落, U32 |
| ItemDropTable | DropItemStack15 | 0.0002 | 2 | 15#物品掉落重合数量, U8 |
| ItemDropTable | DropRate15 | 0.0002 | 2 | 15#掉率, U16 |
| ItemDropWorldTable | TID | 0.96 | 24 | 分离器, U32, 1 |
| ItemDropWorldTable | Desc | 0.96 | 24 | 企划者用, CBwString, 入网券 |
| ItemDropWorldTable | Svr | 0.08 | 2 | 服务器号码, U8 |
| ItemDropWorldTable | DropItemTID | 0.96 | 24 | 下行号码, U32, 9070 |
| ItemDropWorldTable | DropItemStack | 0.96 | 3 | 下行重合号码, U8, 1 |
| ItemDropWorldTable | ItemRate | 0.96 | 9 | 下行率, U16, 50 |
| ItemDropWorldTable | EventType | 0.96 | 3 | 活动用?(0:基本,1:一般活动,2:网吧活动), U8, 0 |
| ItemDropWorldTable | MinPLevel | 0.96 | 8 | PC?? ??(??), U8, 0 |
| ItemDropWorldTable | MaxPLevel | 0.96 | 7 | PC等级 最大(饱和), U8, 0 |
| ItemEnchantGlowTable | TID | 1.0 | 98 | 分离器, 2, U32 |
| ItemEnchantGlowTable | Comment | 0.9899 | 15 | 企划者用, CBwString, 垃圾(灰色) |
| ItemEnchantGlowTable | Grade | 0.9899 | 8 | 物品等级, U8, 0 |
| ItemEnchantGlowTable | Step | 0.9899 | 18 | 强化阶段, U8, 0 |
| ItemEnchantGlowTable | Power | 0.9899 | 6 | 成长强度(0.1~1为止), F32, 0 |
| ItemEnchantGlowTable | Color | 0.9899 | 10 | 成长颜色, string, 0 |
| ItemEnchantTable | TID | 0.9997 | 3681 | ЧјЗж, U16, 81 |
| ItemEnchantTable | GroupTID | 0.9997 | 249 | ЭХЖг ID, U16, 80 |
| ItemEnchantTable | Step | 0.9997 | 17 | ЧПЛЏНзЖЮ, U8, 1 |
| ItemEnchantTable | Comment | 0.9995 | 251 | ЦѓЛЎепгУ, CBwString, ЧПЛЏЕЅЪжНЃ(ПќЫЙЬи-ШЫРр)-1НзЖЮ |
| ItemEnchantTable | SuccessRate | 0.9997 | 17 | ГЩЙІИХТЪ, U16, 10000 |
| ItemEnchantTable | KeepRate | 0.9997 | 12 | ЮЌГжИХТЪ, U16, 0 |
| ItemEnchantTable | DownRate | 0.9997 | 4 | ЕєТЪ, U16, 0 |
| ItemEnchantTable | ResetRate | 0.9997 | 5 | ГѕЪМЛЏИХТЪ, U16, 0 |
| ItemEnchantTable | CostGhelld | 0.9997 | 205 | ЪжајЗб, U32, 0 |
| ItemEnchantTable | SourceItem01 | 0.9997 | 18 | 1КХВФСЯЮяЦЗTID, U32, 9075 |
| ItemEnchantTable | Item01Value | 0.9997 | 3 | 1КХЮяЦЗИіЪ§, U8, 1 |
| ItemEnchantTable | SourceItem02 | 0.0005 | 2 | 2КХВФСЯЮяЦЗ TID, U32 |
| ItemEnchantTable | Item02Value | 0.0005 | 2 | 2КХЮяЦЗИіЪ§, U8 |
| ItemEnchantTable | STR | 0.9997 | 3 | ЦјСІ, U8, 0 |
| ItemEnchantTable | CON | 0.9997 | 3 | ЬхСІ, U8, 0 |
| ItemEnchantTable | WIS | 0.9997 | 3 | жЧЛл, U8, 0 |
| ItemEnchantTable | MEN | 0.9997 | 3 | ОЋЩёСІ, U8, 0 |
| ItemEnchantTable | AGI | 0.9997 | 3 | УєНн, U8, 0 |
| ItemEnchantTable | HPFixed | 0.9997 | 43 | зюДѓHP, S32, 0 |
| ItemEnchantTable | HPR | 0.9997 | 31 | HPЛиИДСП, S32, 0 |
| ItemEnchantTable | HPRBuff | 0.9997 | 3 | HP зЗМгЛиИДСП, S32, 0 |
| ItemEnchantTable | MPFixed | 0.9997 | 42 | зюДѓMP, S32, 0 |
| ItemEnchantTable | MPR | 0.9997 | 31 | MPЛиИДСП, S32, 0 |
| ItemEnchantTable | MPRBuff | 0.9997 | 3 | MP зЗМгЛиИДСП, S32, 0 |
| ItemEnchantTable | POPMin | 0.9997 | 226 | зюаЁЮяРэЙЅЛїЧПЖШ, U32, 4 |
| ItemEnchantTable | POPMax | 0.9997 | 226 | зюДѓЮяРэЙЅЛїЧПЖШ, U32, 4 |
| ItemEnchantTable | MOPMin | 0.9997 | 138 | зюаЁФЇЗЈЙЅЛїЧПЖШ, U32, 0 |
| ItemEnchantTable | MOPMax | 0.9997 | 138 | зюДѓФЇЗЈЙЅЛїЧПЖШ, U32, 0 |
| ItemEnchantTable | PD | 0.9997 | 283 |  ЮяРэЗРгљ, U32, 0 |
| ItemEnchantTable | MD | 0.9997 | 279 | ФЇЗЈЗРгљ, U32, 0 |
| ItemEnchantTable | FD | 0.9997 | 3 | Л№ЪєадЕжПЙ, U32, 0 |
| ItemEnchantTable | WD | 0.9997 | 3 | ЫЎЪєадЕжПЙ, U32, 0 |
| ItemEnchantTable | AD | 0.9997 | 3 | ЙЅЛїЪєадЕжПЙ, U32, 0 |
| ItemEnchantTable | LD | 0.9997 | 3 | ЭСЪєадЕжПЙ, U32, 0 |
| ItemEnchantTable | AP | 0.9997 | 43 | УќжаТЪ, U8, 0 |
| ItemEnchantTable | DP | 0.9997 | 3 | ЩСБмЖШ, U8, 0 |
| ItemEnchantTable | BP | 0.9997 | 74 | РЙНиЖШ, U8, 0 |
| ItemEnchantTable | CP | 0.9997 | 47 | жТУќвЛЛї, U8, 0 |
| ItemEnchantTable | IGN_AT | 0.9997 | 31 | ЗРгљЮфЦїЖШ, U16, 0 |
| ItemEnchantTable | PvP_AT | 0.9997 | 3 | PvPЙЅЛїСІ, F32, 0 |
| ItemEnchantTable | PvP_DF | 0.9997 | 3 | PvPЗРгљСІ, F32, 0 |
| ItemEnchantTable | AS | 0.9997 | 11 | ЙЅЛїЫйЖШ, U16, 0 |
| ItemEnchantTable | RS | 0.9997 | 3 | вЦЖЏЫйЖШ, U16, 0 |
| ItemEnchantTable | CS | 0.9997 | 3 | ЪЉЗЈЫйЖШ, U16, 0 |
| ItemMatrixTable | WeaponName | 1.0 | 167 | 武器名, 2, string |
| ItemMatrixTable | CharName | 1.0 | 22 | 模特名, 2, string |
| ItemMatrixTable | HandType | 1.0 | 5 | 手位置, 2, CBwString |
| ItemMatrixTable | TX | 1.0 | 197 | X轴心动, 2, F32 |
| ItemMatrixTable | TY | 1.0 | 197 | Y轴心动, 2, F32 |
| ItemMatrixTable | TZ | 1.0 | 198 | Z轴心动, 2, F32 |
| ItemMatrixTable | RX | 1.0 | 155 | X轴心转动, 2, F32 |
| ItemMatrixTable | RY | 1.0 | 152 | Y轴心转动, 2, F32 |
| ItemMatrixTable | RZ | 1.0 | 155 | Z轴心转动, 2, F32 |
| ItemMatrixTable | Scale | 1.0 | 22 | 大小调节, 2, F32 |
| ItemMatrixTable | CombatScale | 1.0 | 29 | 战斗模式比例, 2, F32 |
| ItemMixTable | TID | 0.9848 | 65 | 分离器, U32, 1 |
| ItemMixTable | Comment | 0.9848 | 65 | 企划者用, CBwString, 最低级古代精灵石: 武器 |
| ItemMixTable | SourceItem01 | 0.7576 | 4 | 需要物品TID, U32, 90024 |
| ItemMixTable | SourceItemCount01 | 0.7576 | 3 | 需要物品个数, U16, 1 |
| ItemMixTable | MixRate01 | 0.9848 | 4 | 1号组合时概率值, U16, 2000 |
| ItemMixTable | MixItemResult01 | 0.9848 | 65 | 1号成品 TID, U32, 90027 |
| ItemMixTable | MixItemCount01 | 0.9848 | 3 | 1号成品个数, U32, 1 |
| ItemMixTable | MixRate02 | 0.2576 | 3 | 2号组合概率值, U16, 4400 |
| ItemMixTable | MixItemResult02 | 0.2576 | 17 | 2号 成品 TID, U32, 90027 |
| ItemMixTable | MixItemCount02 | 0.2576 | 3 | 2号 成品个数, U32, 1 |
| ItemMixTable | MixRate03 | 0.2576 | 3 | 3号组合概率值, U16, 7000 |
| ItemMixTable | MixItemResult03 | 0.2576 | 17 | 3号 成品 TID, U32, 90027 |
| ItemMixTable | MixItemCount03 | 0.2576 | 3 | 3号 成品个数, U32, 1 |
| ItemMixTable | MixRate04 | 0.0303 | 2 | 4号组合概率值, U16 |
| ItemMixTable | MixItemResult04 | 0.0303 | 2 | 4号 成品 TID, U32 |
| ItemMixTable | MixItemCount04 | 0.0303 | 2 | 4号 成品个数, U32 |
| ItemMixTable | MixRate05 | 0.0303 | 2 | 5号组合概率值, U16 |
| ItemMixTable | MixItemResult05 | 0.0303 | 2 | 5号 成品 TID, U32 |
| ItemMixTable | MixItemCount05 | 0.0303 | 2 | 5号 成品个数, U32 |
| ItemSeedTable | TID | 0.9945 | 182 | 分离器, U16, 1 |
| ItemSeedTable | Comment | 0.9945 | 182 | 企划者用, CBwString, 一般_分身_头盔_交易1 |
| ItemSeedTable | Group | 0.9945 | 20 | 团队值, U16, 1 |
| ItemSeedTable | CashRate | 0.9945 | 15 | SID高速缓存概率值, U16, 1500 |
| ItemSeedTable | GhelldRate | 0.9945 | 12 | 货币获取概率值, U16, 1584 |
| ItemSeedTable | Quality | 0.9945 | 5 | 品质值, U8, 0 |
| ItemSeedTable | STR | 0.9945 | 6 | 气力, U8, 0 |
| ItemSeedTable | CON | 0.9945 | 6 | 体力, U8, 0 |
| ItemSeedTable | WIS | 0.9945 | 6 | 理智, U8, 0 |
| ItemSeedTable | MEN | 0.9945 | 6 | 精神力, U8, 0 |
| ItemSeedTable | AGI | 0.9945 | 6 | 敏捷, U8, 0 |
| ItemSeedTable | HPFixed | 0.9945 | 9 | HP固定上升, S32, 105 |
| ItemSeedTable | HPR | 0.9945 | 6 | HP回复量, S32, 0 |
| ItemSeedTable | HPRBuff | 0.9945 | 6 | HP 追加回复量, S32, 0 |
| ItemSeedTable | MPFixed | 0.9945 | 6 | MP固定上升, S32, 0 |
| ItemSeedTable | MPR | 0.9781 | 8 | MP回复量, S32, 0 |
| ItemSeedTable | MPRBuff | 0.9945 | 3 | MP追加回复量, S32, 0 |
| ItemSeedTable | POPMin | 0.9945 | 6 | 最小物理攻击, U32, 0 |
| ItemSeedTable | POPMax | 0.9945 | 6 | 最大物理攻击, U32, 0 |
| ItemSeedTable | MOPMin | 0.9945 | 6 | 最小魔法攻击, U32, 0 |
| ItemSeedTable | MOPMax | 0.9945 | 6 | 最大魔法攻击, U32, 0 |
| ItemSeedTable | PD | 0.9945 | 9 | 物理防御力, U32, 234 |
| ItemSeedTable | MD | 0.9945 | 6 | 魔法防御, U32, 0 |
| ItemSeedTable | AP | 0.9454 | 8 | 命中度, U16, 0 |
| ItemSeedTable | DP | 0.9945 | 6 | 闪避度, U16, 0 |
| ItemSeedTable | BP | 0.9945 | 6 | 减免伤害度, U16, 0 |
| ItemSeedTable | CP | 0.9945 | 6 | 致命一击, U16, 0 |
| ItemSeedTable | IGN_AT | 0.9945 | 3 | 无视防御伤害, U16, 0 |
| ItemSeedTable | PvP_AT | 0.9945 | 3 | PvP攻击力, F32, 0 |
| ItemSeedTable | PvP_DF | 0.9945 | 3 | PvP防御力, F32, 0 |
| ItemSeedTable | AS | 0.9945 | 3 | 攻击速度, U16, 0 |
| ItemSeedTable | RS | 0.9945 | 3 | 移动速度, U16, 0 |
| ItemSeedTable | CS | 0.9945 | 3 | 施法速度, U16, 0 |
| ItemSetAbilityTable | TID | 0.9988 | 840 | 分离器, U16, 1 |
| ItemSetAbilityTable | Comment | 0.9988 | 184 | 套装名(企划者用), CBwString, 高级-1献身的洛夫套装(Lv.10) |
| ItemSetAbilityTable | ReqTotal | 0.9988 | 7 | 需要个数, U8, 2 |
| ItemSetAbilityTable | STR | 0.9988 | 27 | 气力, U8, 0 |
| ItemSetAbilityTable | CON | 0.9988 | 24 | 体力, U8, 0 |
| ItemSetAbilityTable | WIS | 0.9988 | 15 | 智慧, U8, 0 |
| ItemSetAbilityTable | MEN | 0.9988 | 23 | 智力, U8, 0 |
| ItemSetAbilityTable | AGI | 0.9988 | 21 | 敏捷, U8, 0 |
| ItemSetAbilityTable | HPFixed | 0.9988 | 15 | 最大 HP, S32, 0 |
| ItemSetAbilityTable | HPR | 0.9988 | 15 | HP回复量, S32, 0 |
| ItemSetAbilityTable | HPRBuff | 0.9988 | 17 | HP追加回复量, S32, 0 |
| ItemSetAbilityTable | MPFixed | 0.9988 | 15 | 最大MP, S32, 0 |
| ItemSetAbilityTable | MPR | 0.9988 | 25 | MP回复量, S32, 0 |
| ItemSetAbilityTable | MPRBuff | 0.9988 | 3 | MP追加回复量, S32, 0 |
| ItemSetAbilityTable | POPMin | 0.9988 | 15 | 最小物理攻击, U32, 0 |
| ItemSetAbilityTable | POPMax | 0.9988 | 15 | 最大物理攻击, U32, 0 |
| ItemSetAbilityTable | MOPMin | 0.9988 | 15 | 最小魔法攻击, U32, 0 |
| ItemSetAbilityTable | MOPMax | 0.9988 | 15 | 最大魔法攻击, U32, 0 |
| ItemSetAbilityTable | PD | 0.9988 | 33 | 物理防御, U32, 0 |
| ItemSetAbilityTable | MD | 0.9988 | 33 | 魔法防御, U32, 0 |
| ItemSetAbilityTable | FD | 0.9988 | 3 | 火属性抵抗, U32, 0 |
| ItemSetAbilityTable | WD | 0.9988 | 3 | 水属性抵抗, U32, 0 |
| ItemSetAbilityTable | AD | 0.9988 | 3 | 攻击属性抵抗, U32, 0 |
| ItemSetAbilityTable | LD | 0.9988 | 3 | 土属性抵抗, U32, 0 |
| ItemSetAbilityTable | AP | 0.9988 | 15 | 命中度, U8, 0 |
| ItemSetAbilityTable | DP | 0.9988 | 20 | 闪避度, U8, 0 |
| ItemSetAbilityTable | BP | 0.9988 | 15 | 拦截度, U8, 0 |
| ItemSetAbilityTable | CP | 0.9988 | 25 | 致命一击, U8, 0 |
| ItemSetAbilityTable | IGN_AT | 0.9988 | 5 | 防御武器攻击力, U16, 0 |
| ItemSetAbilityTable | PvP_AT | 0.9988 | 5 | PvP攻击力, F32, 0 |
| ItemSetAbilityTable | PvP_DF | 0.9988 | 5 | PvP防御力, F32, 0 |
| ItemSetAbilityTable | AS | 0.9988 | 18 | 攻击速度, U16, 0 |
| ItemSetAbilityTable | RS | 0.9988 | 6 | 移动速度, U16, 0 |
| ItemSetAbilityTable | CS | 0.9988 | 3 | 施法速度, U16, 0 |
| ItemSetAbilityTable | EngDesc | 0.0024 | 2 | 英文说明, CBwString |
| ItemSetAbilityTable | LocalDesc | 0.9988 | 271 | 韩文说明, CBwString, 2套装：无 |
| ItemSetTable | TID | 0.9972 | 352 | 分离器, U16, 1 |
| ItemSetTable | Comment | 0.9972 | 352 | 套装名(企划者用）, CBwString, 高级-牺牲之罗布套装(Lv.30) |
| ItemSetTable | ItemTID | 0.9972 | 352 | 物品 TID, U32:v, 100000|100001|100002|100003|100004|100005 |
| ItemSetTable | SetAbilityTID | 0.9972 | 184 | 套装能力值 TID, U16:v, 1|2|3|4|5 |
| ItemSocketTable | TID | 0.9 | 9 | 区分, U32, 1 |
| ItemSocketTable | EquipCostGhelld | 0.9 | 9 | 装备手续费, U32, 100 |
| ItemSocketTable | RemoveCostGhelld | 0.9 | 9 | 分离手续费, U32, 100 |
| ItemSocketTable | SuccessRate | 0.9 | 9 | 成功概率, U16, 9000 |
| ItemSocketTable | KeepRate | 0.9 | 3 | 维持概率, U16, 0 |
| ItemSocketTable | Comment | 0.8 | 8 | 说明, CBwString, 最低级 |
| ItemTable | TID | 1.0 | 25165 | TID, U32, 1 |
| ItemTable | Comment | 0.94 | 574 | 私用, CBwString,  通用 |
| ItemTable | EngName | 0.9929 | 24987 | 英文名(32字), CBwString, ITM_Name_000001 |
| ItemTable | LocalName | 1.0 | 13962 | 韩字名(32字), CBwString, 测试防具(提示测试) |
| ItemTable | Type | 1.0 | 16 | 类型, U8, 1 |
| ItemTable | Kind | 1.0 | 16 | 种类, U8, 1 |
| ItemTable | Property | 1.0 | 4 | 属性, U8, 0 |
| ItemTable | Level | 1.0 | 62 | 道具等级, U8, 2 |
| ItemTable | Grade | 1.0 | 8 | 等级, U8, 5 |
| ItemTable | Race | 1.0 | 10 | 种族限制, U8:v, 3 |
| ItemTable | Gender | 1.0 | 3 | 性别限制, U8, 0 |
| ItemTable | LimitLevel | 1.0 | 58 | 等级限制, U8, 2 |
| ItemTable | LimitSTR | 1.0 | 4 | 力量限制, U16, 2 |
| ItemTable | LimitCON | 1.0 | 4 | 材料限制, U16, 3 |
| ItemTable | LimitWIS | 1.0 | 4 | 技能限制, U16, 4 |
| ItemTable | LimitMEN | 1.0 | 5 | 精神力的限制, U16, 5 |
| ItemTable | LimitAgility | 1.0 | 4 | 敏捷的限制, U16, 6 |
| ItemTable | LimitMainWeapon | 0.0001 | 2 | 主武器限制, U8:v |
| ItemTable | LimitFamePointTID | 1.0 | 5 | 名望点数限制, U8, 0 |
| ItemTable | ReqWeaponLevel | 1.0 | 29 | 需要武器熟练度等级, U8, 20 |
| ItemTable | PenaltyRate | 1.0 | 4 | 惩罚, U8, 0 |
| ItemTable | Area | 1.0 | 278 | 可使用的靴子域, U32, 0 |
| ItemTable | PowerRangeMax | 0.9999 | 3 | 最大攻击距离, U16, 0 |
| ItemTable | RelativeClass | 1.0 | 4 | 能力值相对值无, U8, 0 |
| ItemTable | STR | 0.9999 | 19 | 力量, U8, 2 |
| ItemTable | CON | 0.9999 | 19 | 体力, U8, 2 |
| ItemTable | WIS | 0.9999 | 19 | 智能, U8, 2 |
| ItemTable | MEN | 0.9999 | 19 | 精神力, U8, 2 |
| ItemTable | AGI | 0.9999 | 19 | 敏捷, U8, 2 |
| ItemTable | HPFixed | 1.0 | 275 | HP固定上升, S32, 30 |
| ItemTable | HPR | 1.0 | 42 | HP恢复量, S32, 5 |
| ItemTable | HPRBuff | 1.0 | 57 | HP 额外回复量, S32, 0 |
| ItemTable | MPFixed | 1.0 | 314 | MP固定上升, S32, 50 |
| ItemTable | MPR | 1.0 | 39 | MP恢复量, S32, 10 |
| ItemTable | MPRBuff | 1.0 | 15 | MP 额外回复量, S32, 0 |
| ItemTable | POPMin | 1.0 | 322 | 最小物理攻击, U32, 5 |
| ItemTable | POPMax | 1.0 | 371 | 最大物理攻击, U32, 10 |
| ItemTable | MOPMin | 1.0 | 322 | 最小魔法攻击, U32, 15 |
| ItemTable | MOPMax | 1.0 | 362 | 最大魔法攻击, U32, 20 |
| ItemTable | PD | 1.0 | 1507 | 物理防御度, U32, 4 |
| ItemTable | MD | 1.0 | 1483 | 魔法防御度, U32, 3 |
| ItemTable | FD | 1.0 | 15 | 火属性抗性, U32, 0 |
| ItemTable | WD | 1.0 | 15 | 水属性抗性, U32, 0 |
| ItemTable | AD | 1.0 | 15 | 空气阻力属性, U32, 0 |
| ItemTable | LD | 1.0 | 15 | 土地属性抵抗, U32, 0 |
| ItemTable | AP | 1.0 | 105 | 命中度, U16, 2 |
| ItemTable | DP | 1.0 | 28 | 回避度, U16, 3 |
| ItemTable | BP | 1.0 | 174 | 伤害减少度, U16, 4 |
| ItemTable | CP | 1.0 | 62 | 致命度, U16, 5 |
| ItemTable | IGN_AT | 1.0 | 117 | 无视防御攻击, U16, 6 |
| ItemTable | PvP_AT | 1.0 | 35 | PvP攻击力, F32, 0 |
| ItemTable | PvP_DF | 1.0 | 34 | PvP防御力, F32, 0 |
| ItemTable | AS | 1.0 | 71 | 攻击速度, U16, 7 |
| ItemTable | RS | 1.0 | 23 | 移动速度, U16, 8 |
| ItemTable | CS | 1.0 | 3 | 施法速度, U16, 0 |
| ItemTable | SetTID | 1.0 | 367 | 套装 TID, U16, 0 |
| ItemTable | CoolTime | 1.0 | 5 | 道具冷却时间, U32, 0 |
| ItemTable | UseSkillTID | 1.0 | 411 | 使用技能 TID, U32, 0 |
| ItemTable | LearnSkillTID | 1.0 | 29 | 学习技能 TID, U32, 0 |
| ItemTable | SocketTID | 1.0 | 10 | 插槽 TID, U32, 0 |
| ItemTable | Socket | 1.0 | 6 | 插槽数, U8, 5 |
| ItemTable | CashSocket | 1.0 | 4 | 古代插槽数, U8, 1 |
| ItemTable | RecipeTID | 0.9999 | 3813 | 食谱 TID, U32, 0 |
| ItemTable | EnchantTID | 1.0 | 204 | 强化计算, U16, 12700 |
| ItemTable | EnchantStepMax | 1.0 | 10 | 最大强化阶段, U8, 15 |
| ItemTable | SeedOption | 1.0 | 21 | 种子选项, U16, 0 |
| ItemTable | Cash | 1.0 | 4 | 缓存道具, U8, 0 |
| ItemTable | SpecialTID | 0.9999 | 24 | 特别号码(41=背包扩展 ，42 =仓库包的扩展), U16, 0 |
| ItemTable | SpecialValue | 0.0263 | 72 | 特殊值, S64, 0 |
| ItemTable | AlchemyValue | 0.0131 | 14 | 炼金术的价值, U16, 0 |
| ItemTable | AlchemyTID | 0.0081 | 21 | 炼金术 TID 号码, U32, 0 |
| ItemTable | MixTID | 1.0 | 66 | 组合 TID, U32, 0 |
| ItemTable | BreakTID | 1.0 | 315 | 分解 TID, U32, 0 |
| ItemTable | BoxTID | 1.0 | 305 | 箱子 TID, U16, 0 |
| ItemTable | QuestTID | 1.0 | 135 | 任务 TID 引用, U32, 0 |
| ItemTable | SalePrice | 1.0 | 557 | 售价, U32, 16 |
| ItemTable | PurchasePrice | 1.0 | 564 | 购价, U32, 160 |
| ItemTable | SaleFamePoint | 1.0 | 35 | 名望销售价格, U32, 100 |
| ItemTable | PurchaseFamePoint | 1.0 | 38 | 名望购买价格, U32, 0 |
| ItemTable | ReqMedalKind | 1.0 | 8 | 购买/销售 奖章类型, U8, 0 |
| ItemTable | SaleMedal | 1.0 | 8 | 销售奖牌数量, U32, 0 |
| ItemTable | PurchaseMedal | 1.0 | 28 | 购买奖牌数量, U32, 0 |
| ItemTable | ItemRestrict | 0.9999 | 7 | 道具限制, U32, 15 |
| ItemTable | StackCount | 0.9999 | 10 | 每列数, U32, 0 |
| ItemTable | MaxCount | 0.9999 | 3 | 最大数量, U32, 0 |
| ItemTable | Consume | 0.9999 | 4 | 道具是否消耗, U8, 0 |
| ItemTable | BindType | 1.0 | 5 | 归属配置, U8, 0 |
| ItemTable | UnBindCount | 1.0 | 6 | 归属解除可能次数, U8, 0 |
| ItemTable | Stoppable | 0.9999 | 3 | 是否可以停止, U8, 0 |
| ItemTable | MaxDurability | 1.0 | 70 | 最大耐久度, U16, 48 |
| ItemTable | MinDurability | 1.0 | 4 | 最大耐久度减少限制值, U16, 10 |
| ItemTable | Crash | 1.0 | 3 | 耐久度为0时 道具戴穆里申/无, U8, 0 |
| ItemTable | DecreationDurability | 1.0 | 7 | 减少维修的最大耐久度值, U8, 10 |
| ItemTable | Repairable | 1.0 | 4 | 修理可能/无, U8, 1 |
| ItemTable | ItemMeshLeft | 0.5389 | 949 | 物品文件(64字), string:v, p_h_01_i_m_helm_lod.nif |
| ItemTable | ItemMeshRight | 0.5569 | 972 | 道具文件(64字), string:v, p_h_01_i_f_helm_lod.nif |
| ItemTable | ItemMeshScale | 0.0001 | 2 | 装备武器的尺寸, F32 |
| ItemTable | UseEffect | 0.1959 | 20 |  使用物品效果, CBwString, 50_001 |
| ItemTable | UseSound | 0.0001 | 2 |  使用物品的, string |
| ItemTable | TreeDeps_01 | 1.0 | 11 | 拍卖树按钮1号, U8, 99 |
| ItemTable | TreeDeps_02 | 1.0 | 17 | 拍卖树按钮2号, U8, 0 |
| ItemTable | ItemIcon | 1.0 | 1663 | 图标号, U32, 1 |
| ItemTable | EngDesc | 0.9928 | 24986 | 英文物品描述(256字), CBwString, ITM_Desc_000001 |
| ItemTable | LocalDesc | 0.2768 | 5915 | 韩字 下载的物品说明(256字), CBwString, 说明:测试用者1阶段头盔A |
| LevelCompareTable | TID | 1.0 | 23 | 索引, 1, U8 |
| LevelCompareTable | Compare | 1.0 | 23 | 等级差别, 1, S16 |
| LevelCompareTable | PC2PC_HitPoint | 1.0 | 3 | PC 等级基准 PvP 命中率差别, 1, F32 |
| LevelCompareTable | PC2NPC_HitPoint | 1.0 | 3 | PC 等级基准 命中率 差别, 1, F32 |
| LevelCompareTable | NPC2PC_HitPoint | 1.0 | 8 | NPC 等级基准 命中率差别, 1, F32 |
| LevelCompareTable | NPC2NPC_HitPoint | 1.0 | 8 | NPC对NPC 等级基准 命中率差别, 1, F32 |
| LevelCompareTable | PC2PC_Attack | 1.0 | 3 | PC 等级基准 PvP 伤害差别, 1, F32 |
| LevelCompareTable | PC2NPC_Attack | 1.0 | 3 | PC 等级基准 伤害差别, 1, F32 |
| LevelCompareTable | NPC2PC_Attack | 1.0 | 3 | NPC 等级基准 伤害差别, 1, F32 |
| LevelCompareTable | NPC2NPC_Attack | 1.0 | 13 | NPC对NPC 等级基准 伤害差别, 1, F32 |
| LevelCompareTable | PC_WeaponExp | 1.0 | 9 | PC 等级基准 武器熟练度差别, 1, F32 |
| LevelCompareTable | PC_Drop | 1.0 | 8 | PC 等级基准 物品掉率差别, 1, F32 |
| LevelCompareTable | PC_Exp | 1.0 | 6 | PC 等级基准 获得经验值差别, 1, F32 |
| LevelCompareTable | PC_Ghelld | 1.0 | 8 | PC 等级基准 盖尔德量差别, 1, F32 |
| LevelCompareTable | PC_GatherExp | 1.0 | 4 | 采集熟练度 等级差别, 1, F32 |
| LevelCompareTable | PC_GatherProba | 1.0 | 8 | 采集成功率差别, 1, F32 |
| LevelupTable | TID | 1.0 | 402 | 人物号码, 1, U16 |
| LevelupTable | Race | 1.0 | 6 | 种族, 1, U8 |
| LevelupTable | Level | 1.0 | 102 | 等级, 1, U8 |
| LevelupTable | Exp | 1.0 | 103 | 下级经验值, 1, S64 |
| LevelupTable | TotalExp | 1.0 | 103 | 综合经验值, 1, S64 |
| LevelupTable | AcquisitionStatPoint | 1.0 | 5 | 获得积分点, 1, U8 |
| LevelupTable | ResetStatPoint | 1.0 | 103 | 积分重置, 1, U8 |
| LevelupTable | HP | 1.0 | 103 | HP增加量, 1, S32 |
| LevelupTable | MP | 1.0 | 103 | MP增加量, 1, S32 |
| LevelupTable | HPRBuff | 1.0 | 4 | HP 追加回复量, 1, S32 |
| LevelupTable | MPRBuff | 1.0 | 4 | MP 追加回复量, 1, S32 |
| LevelupTable | DP | 1.0 | 4 | 躲闪度增加量, 1, U8 |
| LevelupTable | BP | 1.0 | 4 | 拦截度增加量, 1, U8 |
| LevelupTable | AP | 1.0 | 4 | 命中度增加量, 1, U8 |
| LocalizeTable | TID | 1.0 | 23 | 桌子名, 2, CBwString |
| LocalizeTable | Column | 1.0 | 15 | 色彩名, 2, CBwString:v |
| LocalizeTable | Pos | 1.0 | 16 | 色彩位置, 2, S32:v |
| LocalizeTable | Desc | 0.1304 | 3 | 说明, 2, CBwString |
| MailTable | TID | 1.0 | 51 | Tid, 1, U32 |
| MailTable | Type | 1.0 | 7 | 类型, 1, U8 |
| MailTable | Kind | 1.0 | 6 | 种类, 1, U8 |
| MailTable | Value | 0.9808 | 12 | 值, 1, U8 |
| MailTable | ToRealm | 1.0 | 5 | 遭受的阵营, 1, U8 |
| MailTable | Property | 1.0 | 3 | 属性, 1, U8 |
| MailTable | Title | 1.0 | 46 | 项目, 1, CBwString |
| MailTable | Main | 1.0 | 28 | 内容, 1, CBwString |
| MailTable | Sender | 1.0 | 5 | 发送人, 1, CBwString |
| MailTable | KeepTerm | 1.0 | 7 | 保管期限, 1, U8 |
| MailTable | AddGhelld | 0.0577 | 3 | 附件货币, 1, U32 |
| MailTable | AddItemTID | 0.8846 | 22 | 附件物品, 1, U32 |
| MailTable | AddItemCount | 0.8846 | 5 | 附件物品数量, 1, U8 |
| MailTable | LocalDesc | 1.0 | 52 | 韩文用途说明, 2, CBwString |
| MapTable | TID | 1.0 | 501 | 分离器, 2, U32 |
| MapTable | WorldTID | 0.998 | 169 | 世界地图TID, U32, 1 |
| MapTable | MapX | 0.998 | 20 | 地图X号码, U32, 0 |
| MapTable | MapY | 0.998 | 20 | 地图Y号码, U32, 0 |
| MapTable | SectorCountX | 0.004 | 2 | 扇形区X个数, U32 |
| MapTable | SectorCountY | 0.004 | 2 | 扇形区Y个数, U32 |
| MapTable | LevelName | 0.3546 | 161 | 韩文名, CBwString, 人物生成(高级) |
| MapTable | Desc | 0.4681 | 4 | 说明, CBwString, 完成 |
| MapTable | Path | 0.998 | 416 | 文件位置, string, Terrain/Loginfield/Create_Amihigh/ |
| MessageBoxTable | TID | 1.0 | 162 | ???id, 2, U16 |
| MessageBoxTable | String | 1.0 | 163 | ???, 2, CBwString |
| MessageBoxTable | EngTitle | 0.9877 | 161 | ?? ???, 2, CBwString |
| MessageBoxTable | LocalTitle | 1.0 | 113 | ?? ???, 2, CBwString |
| MessageBoxTable | EngContents | 0.9877 | 161 | ?? ??, 2, CBwString |
| MessageBoxTable | LocalContents | 1.0 | 161 | ?? ??, 2, CBwString |
| MessageBoxTable | FontColor | 0.9939 | 6 | ???, 2, CBwString |
| MessageBoxTable | FontSize | 0.9939 | 4 | ????, 2, U8 |
| MessageBoxTable | EngDesc | 0.9877 | 161 | ?? ????, 2, CBwString |
| MessageBoxTable | LocalDesc | 0.9816 | 147 | ?? ????, 2, CBwString |
| MessageTable | TID | 1.0 | 2040 | 测试id, 2, U16 |
| MessageTable | Position | 0.9995 | 13 | 输出位置, 2, U16 |
| MessageTable | String | 1.0 | 2027 | 文字列, 2, CBwString |
| MessageTable | EngContents | 0.9956 | 2025 | 英文内容, 2, CBwString |
| MessageTable | LocalContents | 1.0 | 1893 | 内容, 2, CBwString |
| MessageTable | System_Voice | 0.0211 | 31 | 应用输出, 2, CBwString:v |
| MessageTable | FontColor | 1.0 | 43 | 字体颜色, 2, CBwString |
| MessageTable | FontSize | 1.0 | 5 | 字体大小, 2, U8 |
| MessageTable | Comment | 1.0 | 1068 | 开发者用 用途说明, 2, CBwString |
| NaviPointTable | TID | 1.0 | 27335 | 륩蛟포듐, 2, U32 |
| NaviPointTable | WorldTID | 1.0 | 100 | 各썹, U16, 2000 |
| NaviPointTable | Pos | 1.0 | 19177 | 貫零, F32:v, 1780.67|4765.96 |
| NaviPointTable | Link | 1.0 | 27273 | 쌘듐, U32:v, 2|449|11455|11456 |
| NpcBrainTable | TID | 0.9997 | 3209 | ?? ??, U32, 1 |
| NpcBrainTable | Comment | 0.9997 | 2723 | ????, CBwString, Lv.2哥布林(7030) |
| NpcBrainTable | BaseGoal | 0.9994 | 6 | ????, CBwString, wander |
| NpcBrainTable | DetectRadius | 0.9997 | 14 | ?? ??, F32, 0 |
| NpcBrainTable | WanderRadius | 0.9997 | 7 | ?? ??, F32, 10 |
| NpcBrainTable | BattleRadius | 0.9997 | 15 | ?? ??, F32, 40 |
| NpcBrainTable | BattleRestore | 0.9997 | 4 | HP ?? ??, U8, 1 |
| NpcBrainTable | AttackSkill | 0.9081 | 2106 | ????, U32:v, 100001|100002 |
| NpcBrainTable | AttackRate | 0.9081 | 8 | ????, U8:v, 50|50 |
| NpcBrainTable | Action01 | 0.9037 | 1713 | A.I ?? 1?, CBwString:v, MyHP|80|Rate|30|Skill|100003 |
| NpcBrainTable | Action02 | 0.2654 | 497 | A.I ?? 2?, CBwString:v, Die|0|TriggerSkill|200189 |
| NpcBrainTable | Action03 | 0.124 | 348 | A.I ?? 3?, CBwString:v, BattleTime|3|Talk|2 |
| NpcBrainTable | Action04 | 0.0903 | 263 | A.I ?? 4?, CBwString:v, MyHP|80|Skill|122876 |
| NpcBrainTable | Action05 | 0.0642 | 188 | A.I ?? 5?, CBwString:v, MyHP|30|Skill|122876 |
| NpcBrainTable | Action06 | 0.0352 | 67 | A.I ?? 6?, CBwString:v, MyHP|50|Skill|122893 |
| NpcBrainTable | Action07 | 0.0237 | 15 | A.I ?? 7?, CBwString:v, MyHP|10|Skill|122893 |
| NpcBrainTable | Action08 | 0.0262 | 12 | A.I ?? 8?, CBwString:v, MyHP|30|Skill|122896 |
| NpcBrainTable | Action09 | 0.033 | 9 | A.I ?? 9?, CBwString:v, IdleTime|5|Skill|232511 |
| NpcBrainTable | Action10 | 0.2053 | 3 | A.I ?? 10?, CBwString:v, IdleRepeat|10800|Skill|232511 |
| NpcBrainTable | Talk_01 | 0.0639 | 141 | 马风船 1号, CBwString:a:Talk, ~~~ ~~~~ ~~~ ~~~~~ |
| NpcBrainTable | Talk_02 | 0.0364 | 91 | 马风船 2号, CBwString, ~ ~~~ ~~ ~~~ ~~ ~~! |
| NpcBrainTable | Talk_03 | 0.0087 | 28 | 马风船 3号, CBwString, ~~~ ~~~ ~~~~ ~~~! |
| NpcBrainTable | Talk_04 | 0.0022 | 7 | 马风船 4号, CBwString, ~~~… ~~ ~~ ~~~~ ~~~ ~~~~ ~~~ ~~~~. |
| NpcBrainTable | Talk_05 | 0.0012 | 4 | 马风船 5号, CBwString, ~~~ ~~~ ~~ ~~~~~. ~~ ~~ ~~~~~~. |
| NpcDlgStringTable | TID | 1.0 | 726 | 共五种要素构成, 第一种--1:瞄准高处 2:摧毁, 第二种--1:问候 2:技能题目 3:流言, 第三~五种:一系列号码, 2, U16 |
| NpcDlgStringTable | Type | 0.9986 | 23 | 1000: 问候 1001:寻求 1002:想知道的点 1003:返回 1004:无可用物品 1005:信件清单/信件内容 1:商店 2:竞买 3:强化 4:仓库 5:精灵石 6:塑料（未使用） 7:修复 8:公会 9:投注(未使用) 10:分解 11:生产 12:魔力 19:战斗机20: 治疗 22: 组合, U16, 1005 |
| NpcDlgStringTable | TypeCondition | 0.9986 | 9 | 8-1:公会建立 8-2:公会标志 8-3: 公会仓库 8-4:公会捐赠 8-5:公会等级上升 8-6: 公会解散 5-1:精灵石安装 5-2:精灵石去除, U16, 0 |
| NpcDlgStringTable | MinLV | 0.9972 | 3 | U8, 0, 1 |
| NpcDlgStringTable | MaxLV | 0.9986 | 4 | 因为50级以上基本代谢不会出来所以把99级都引入了., U8, 0 |
| NpcDlgStringTable | Race | 0.9972 | 2 | U8, 0 |
| NpcDlgStringTable | EngContents | 0.9835 | 715 | 英文内容, CBwString, NDT_Contents_000001 |
| NpcDlgStringTable | LocalContents | 0.9986 | 702 | 韩文内容, CBwString:v, 关闭 |
| NpcDlgStringTable | EngDesc | 0.9835 | 715 | 英文说明, CBwString, NDT_Desc_000001 |
| NpcDlgStringTable | LocalDesc | 0.0151 | 11 | 韩文说明, CBwString:v, 通过 W,A,S,D键来完成移动./n/n技能可以通过按快捷键K然后把图标拉到插槽内即可注册./n/n发现敌人可通过双击鼠标左键或单击右键来攻击目标. |
| NpcTable | TID | 0.9998 | 4705 | Ыїв§, U32, 300001 |
| NpcTable | Type | 0.9998 | 5 | НЧЩЋДѓЗжРр, U8, 4 |
| NpcTable | Kind | 0.9998 | 20 | НЧЩЋаЁЗжРр, U8, 0 |
| NpcTable | Property | 0.9998 | 7 | НЧЩЋЪєаджЕ, U8, 0 |
| NpcTable | SpecialValue | 0.9998 | 9 | ЬиЪтМлжЕ, U8, 0 |
| NpcTable | Race | 0.9998 | 7 | жжзх, U8, 0 |
| NpcTable | Grade | 0.9998 | 7 | ЕШМЖ, U8, 1 |
| NpcTable | WeaponType | 0.9998 | 3 | ЮфЦїРраЭ, U8, 0 |
| NpcTable | ShapeID | 0.9998 | 578 | ЭтаЮаХЯЂ, U32, 20000 |
| NpcTable | Comment | 0.5489 | 299 | ЦѓЛЎШЫгУ, CBwString,  1КХГЁЕи  ДѓЖМЪаИННќ   |
| NpcTable | EngTitle | 0.986 | 4640 | гЂЮФБъЬтУћГЦ, CBwString, NPT_Title_000001 |
| NpcTable | EngName | 0.986 | 4640 | гЂЮФУћГЦ, CBwString, NPT_Name_000001 |
| NpcTable | LocalTitle | 0.6685 | 407 | КЋЮФБъЬтУћГЦ, CBwString, Lv.1 |
| NpcTable | LocalName | 0.9998 | 2941 | КЋЮФУћГЦ, CBwString, ЩЫКлЯнкх |
| NpcTable | UseIconType | 0.9998 | 6 | ЭМБъТЗЯпЪЧЗёЪЙгУ, U8, 0 |
| NpcTable | WorldMapIcon | 0.9998 | 48 | ЪРНчЕиЭМБъЪОЭМБъ, U32, 0 |
| NpcTable | Level | 0.9998 | 58 | ЕШМЖ, U8, 1 |
| NpcTable | HP | 0.9998 | 434 | ЩњУќЪ§жЕ, S32, 10000 |
| NpcTable | MP | 0.9998 | 4 | ФЇЗЈЪ§жЕ, S32, 100 |
| NpcTable | HPR | 0.9998 | 4 | ЩњУќдйЩњСП, U16, 100 |
| NpcTable | MPR | 0.9998 | 4 | ФЇЗЈдйЩњСП, U16, 100 |
| NpcTable | POPMin | 0.9998 | 246 | зюаЁЮяРэЙЅЛїСІ, U32, 1 |
| NpcTable | POPMax | 0.9998 | 248 | зюДѓЮяРэЙЅЛїСІ, U32, 1 |
| NpcTable | MOPMin | 0.9998 | 246 | зюаЁФЇЗЈЙЅЛїСІ, U32, 0 |
| NpcTable | MOPMax | 0.9998 | 248 | зюДѓФЇЗЈЙЅЛїСІ, U32, 0 |
| NpcTable | PD | 0.9998 | 260 | ЮяРэЗРгљСІ, U32, 0 |
| NpcTable | MD | 0.9998 | 260 | ФЇЗЈЗРгљСІ, U32, 0 |
| NpcTable | FD | 0.9998 | 3 | Л№ЪєадЕжПЙЖШ, U32, 0 |
| NpcTable | WD | 0.9998 | 3 | ЫЎЪєадЕжПЙЖШ, U32, 0 |
| NpcTable | AD | 0.9996 | 3 | ПеЦјЪєадЕжПЙЖШ, U32, 0 |
| NpcTable | LD | 0.9998 | 3 | ЭСЪєадЕжПЙЖШ, U32, 0 |
| NpcTable | DP | 0.9998 | 86 | ЛиБмЖШ, U16, 0 |
| NpcTable | BP | 0.9998 | 98 | ВМРЭЖШ, U16, 0 |
| NpcTable | AP | 0.9998 | 125 | УќжаЖШ, U16, 0 |
| NpcTable | CP | 0.9998 | 69 | жТУќЖШ, U16, 0 |
| NpcTable | IGN_AT | 0.9994 | 3 | ЮоЪгЗРгљЙЅЛїЖШ, U16, 0 |
| NpcTable | AS | 0.9998 | 9 | ЙЅЛїЫйЖШ, U16, 0 |
| NpcTable | Ws | 0.9998 | 47 | аазпЫйЖШ, U16, 0 |
| NpcTable | WsAni | 0.9998 | 47 | АВФнЪЕМЪзпТЗОрРы, U16, 0 |
| NpcTable | RS | 0.9998 | 19 | ХмВНЫйЖШ, U16, 0 |
| NpcTable | RsAni | 0.9998 | 43 | АВФнЪЕМЪХмВНОрРы, U16, 0 |
| NpcTable | CS | 0.9998 | 4 | ЪЉеЙЫйЖШ, U16, 0 |
| NpcTable | Exp | 0.9998 | 279 | О­бщжЕ, S64, 0 |
| NpcTable | ItemDropTID | 0.9996 | 248 | ЯюФПТфЪЕTIDВЮПМ, U16, 0 |
| NpcTable | MapDropTID | 0.9996 | 23 | ЕиЭМТфЪЕTID, U16, 0 |
| NpcTable | SaleTID | 0.9998 | 94 | ЩЬЕъTIDВЮПМ, U8, 0 |
| NpcTable | Motion | 0.9998 | 5 | дЫЖЏБрКХ, U16, 2 |
| NpcTable | EventRange | 0.9998 | 5 | ЛюЖЏДэЮѓжЕ, U8, 2 |
| NpcTable | Color | 0.2903 | 40 | беЩЋ, string, 228,171,130 |
| NpcTable | Width | 0.9998 | 12 | NPCПэЖШ, F32, 0.5 |
| NpcTable | Height | 0.9998 | 25 | NPCИпЖШ, F32, 2.1 |
| NpcTable | Scale | 0.9998 | 21 | NPCГпДч, F32, 1 |
| NpcTable | NpcBrain | 0.9998 | 2431 | A.IРраЭ, U32, 20001 |
| NpcTable | RegenR | 0.9998 | 5 | АыОЖЛжИД, F32, 0 |
| NpcTable | RegenTimeMin | 0.9998 | 22 | зюаЁЛжИДЪБМф, U32, 0 |
| NpcTable | RegenTimeMax | 0.9998 | 19 | зюДѓЛжИДЪБМф, U32, 0 |
| NpcTable | Greeting | 1.0 | 589 | ЮЪКђгя, 0, U16:v |
| NpcTable | Eventlist | 1.0 | 14 | ЛюЖЏАДХЅ, 0, U16:v |
| NpcTable | Gossip | 1.0 | 9 | ДЋЮХ, 0, U16:v |
| NpcTable | GreetVoice | 0.2782 | 310 | NPCЮЪКђЩљвє, CBwString:v, KHC_NPC_Male_Young_AA_16_2.ogg |
| NpcTable | GoodbyeVoice | 0.0323 | 95 | NPCИцБ№Щљвє, CBwString:v, CHW_NPC_Female_Young_BB_01_2.ogg |
| PartyExpTable | TID | 0.9828 | 57 | ЗжРыЦї, U16, 1 |
| PartyExpTable | Level | 0.9828 | 57 | аЁЖгЦНОљЕШМЖ, U8, 1 |
| PartyExpTable | Exp | 0.9828 | 57 | ашвЊО­бщжЕ, S64, 15875 |
| PartyExpTable | SkillTID_01 | 0.9828 | 3 | 1#ММФм TID, U32:a:SkillTID, 230011 |
| PartyExpTable | SkillTID_02 | 0.9828 | 3 | 2#ММФм TID, U32, 230013 |
| PartyExpTable | SkillTID_03 | 0.9828 | 3 | 3#ММФм TID, U32, 230015 |
| PartyExpTable | SkillTID_04 | 0.9828 | 3 | 4#ММФм TID, U32, 230016 |
| PartyExpTable | SkillTID_05 | 0.9828 | 3 | 5#ММФм TID, U32, 230017 |
| PartyExpTable | SkillTID_06 | 0.9828 | 3 | 6#ММФм TID, U32, 0 |
| PartyExpTable | SkillTID_07 | 0.9828 | 3 | 7#ММФм TID, U32, 0 |
| PartyExpTable | SkillTID_08 | 0.9828 | 3 | 8#ММФм TID, U32, 0 |
| PartyExpTable | SkillTID_09 | 0.9828 | 3 | 9#ММФм TID, U32, 0 |
| PartyExpTable | SkillTID_10 | 0.9828 | 3 | 10#ММФм TID, U32, 0 |
| PartyExpTable | InsMapTID | 0.9828 | 9 | МДЪБЕиЭМ TID, U16, 2001 |
| PcTable | TID | 0.9773 | 43 | 分离器, U32, 1 |
| PcTable | Type | 0.9773 | 3 | 人物, U8, 1 |
| PcTable | Kind | 0.9773 | 10 | 人物小分类, U8, 1 |
| PcTable | Race | 0.9773 | 6 | 种族, U8, 1 |
| PcTable | Gen | 0.9773 | 4 | 性别, U8, 1 |
| PcTable | MainWeapon | 0.9773 | 13 | 主武器, U8, 0 |
| PcTable | ShapeID | 0.9773 | 11 | 外型信息, U32, 1 |
| PcTable | Comment | 0.9773 | 11 | 企划者用用途说明, CBwString, 人类男 |
| PcTable | Level | 0.9773 | 3 | 等级, U8, 1 |
| PcTable | STR | 0.9773 | 6 | 气力, U16, 0 |
| PcTable | CON | 0.9773 | 5 | 体力, U16, 0 |
| PcTable | WIS | 0.9773 | 6 | 智慧, U16, 0 |
| PcTable | MEN | 0.9773 | 6 | 技能, U16, 0 |
| PcTable | AGI | 0.9773 | 7 | 邻近, U16, 0 |
| PcTable | HP | 0.9773 | 7 | 生命, S32, 800 |
| PcTable | MP | 0.9773 | 7 | 魔力, S32, 200 |
| PcTable | HPR | 0.9773 | 7 | 生命回复量, U16, 40 |
| PcTable | MPR | 0.9773 | 7 | 魔法回复量, U16, 10 |
| PcTable | HPRBuff | 0.9773 | 4 | HP 追加回复量, S32, 0 |
| PcTable | MPRBuff | 0.9773 | 4 | MP 追加回复量, S32, 0 |
| PcTable | POPMin | 0.9773 | 4 | 最小物理攻击力, U32, 0 |
| PcTable | POPMax | 0.9773 | 4 | 最大物理攻击力, U32, 0 |
| PcTable | MOPMin | 0.9773 | 4 | 最小魔法攻击力, U32, 0 |
| PcTable | MOPMax | 0.9773 | 4 | 最大魔法攻击力, U32, 0 |
| PcTable | PD | 0.9773 | 4 | 物理防御力, U32, 0 |
| PcTable | MD | 0.9773 | 4 | 魔法防御力, U32, 0 |
| PcTable | FD | 0.9773 | 4 | 火元素抗性, U32, 0 |
| PcTable | WD | 0.9773 | 4 | 云元素抗性, U32, 0 |
| PcTable | AD | 0.9773 | 4 | 气元素抗性, U32, 0 |
| PcTable | LD | 0.9773 | 4 | 土元素抗性, U32, 0 |
| PcTable | DP | 0.9773 | 4 | 闪躲, U8, 6 |
| PcTable | BP | 0.9773 | 3 | 拦截度, U8, 0 |
| PcTable | AP | 0.9773 | 4 | 命中度, U8, 7 |
| PcTable | CP | 0.9773 | 4 | 致命一击, U8, 8 |
| PcTable | IGN_AT | 0.9773 | 3 | 防御武器攻击度, U16, 0 |
| PcTable | PvP_AT | 0.9773 | 3 | PvP攻击力, F32, 0 |
| PcTable | PvP_DF | 0.9773 | 3 | PvP防御力, F32, 0 |
| PcTable | AS | 0.9773 | 3 | 攻击速度, U16, 1000 |
| PcTable | RS | 0.9773 | 4 | 移动速度, U16, 5000 |
| PcTable | CS | 0.9773 | 3 | 施法速度, U16, 1000 |
| PcTable | Motion | 0.9773 | 3 | 动作号, U16, 1 |
| PcTable | Width | 0.9773 | 3 | PC 面积大小, F32, 0.5 |
| PcTable | Height | 0.9773 | 5 | PC 高度大小, F32, 2 |
| PcTable | Scale | 0.9773 | 3 | PC size, F32, 1 |
| PortalTable | TID | 0.9959 | 242 | 分隔符, U16, 1 |
| PortalTable | Comment | 0.9959 | 54 | 私用, CBwString, 斯蒂尔普瑞斯 逃脱 |
| PortalTable | EngName | 0.9959 | 238 | 英文逃脱名字, CBwString, PTT_Name_000001 |
| PortalTable | LocalName | 0.9959 | 57 | 逃脱名字, CBwString, 尖塔村庄 逃脱 |
| PortalTable | SrcEntityTID | 0.9959 | 54 | 出发地点EntityTID, U32, 101000 |
| PortalTable | DstEntityTID | 0.9959 | 54 | 到达地点EntityTID, U32, 101001 |
| PortalTable | DstWorldPlaceTID | 0.9959 | 54 | 到达地点WorldPlaceTID, U32, 3086 |
| PortalTable | Radius | 0.9959 | 3 | 逃脱范围, F32, 1 |
| PortalTable | reqRace | 0.9959 | 4 | 0:不可使用（不） 1:人类 2:月精灵 4:龙之复仇者 8:兽人//比特运算, U8, 5 |
| PortalTable | reqMinLV | 0.9959 | 3 | 使用最小级别, U8, 1 |
| PortalTable | reqMaxLV | 0.9959 | 3 | 使用最大级别, U8, 99 |
| PortalTable | reqQuest | 0.9959 | 3 | 需要的探索, U32, 0 |
| PortalTable | reqMoney | 0.9959 | 19 | 需要的钱, S64, 90 |
| PortalTable | reqItem | 0.9959 | 3 | 需要的的消费物品 , U32, 0 |
| PortalTable | reqItemCount | 0.9959 | 3 | 需要的消费物品数, U32, 0 |
| PortalTable | reqHaveItem | 0.9959 | 3 | 需要的携带道具, U32, 0 |
| PortalTable | reqHaveItemCount | 0.9959 | 3 | 需要携带的物品数, U32, 0 |
| ProductItemTable | TID | 0.9997 | 3812 | 标识号, U16, 1001 |
| ProductItemTable | ProductType | 0.9997 | 7 | 配方类产品种类, U8, 1 |
| ProductItemTable | ProductKind | 0.9997 | 15 | 完成品的种类, U8, 1 |
| ProductItemTable | Comment | 0.9997 | 2073 | 项目号码的规划作用, CBwString, 模式：破旧的枪 |
| ProductItemTable | ItemTID | 0.9997 | 3812 | 项目号码作用, U32, 60000 |
| ProductItemTable | ProductLevel | 0.9997 | 57 | 所需的技能等级, U8, 1 |
| ProductItemTable | RecipeExp | 0.9997 | 159 | 经验获得的最大额, U32, 230 |
| ProductItemTable | CostGhelld | 0.9997 | 333 | 手续费, U32, 300 |
| ProductItemTable | CompleteItemTID | 0.9997 | 3743 | 完成项目, U32, 1010251 |
| ProductItemTable | SourceItem01 | 0.9997 | 48 | 01#材料项目, U32, 37100 |
| ProductItemTable | Value01 | 0.9997 | 24 | 01#材料统计, U16, 9 |
| ProductItemTable | SourceItem02 | 0.8594 | 59 | 02#材料项目, U32, 42000 |
| ProductItemTable | Value02 | 0.8594 | 14 | 02#材料统计, U16, 1 |
| ProductItemTable | SourceItem03 | 0.6134 | 11 | 03#材料项目, U32, 42005 |
| ProductItemTable | Value03 | 0.6134 | 40 | 03#材料统计, U16, 1 |
| ProductItemTable | SourceItem04 | 0.3706 | 6 | 04#材料项目, U32, 39100 |
| ProductItemTable | Value04 | 0.3706 | 13 | 04#材料统计, U16, 1 |
| ProductItemTable | SourceItem05 | 0.0005 | 2 | 05#材料项目, U32 |
| ProductItemTable | Value05 | 0.0005 | 2 | 05#材料统计, U16 |
| ProductItemTable | SourceItem06 | 0.0005 | 2 | 06#材料项目, U32 |
| ProductItemTable | Value06 | 0.0005 | 2 | 06#材料统计, U16 |
| ProductItemTable | SourceItem07 | 0.0005 | 2 | 07#材料项目, U32 |
| ProductItemTable | Value07 | 0.0005 | 2 | 07#材料统计, U16 |
| ProductItemTable | SourceItem08 | 0.0005 | 2 | 08#材料项目, U32 |
| ProductItemTable | Value08 | 0.0005 | 2 | 08#材料统计, U16 |
| ProductLvTable | TID | 1.0 | 443 | 人物, 0, U16 |
| ProductLvTable | ProductType | 1.0 | 11 | 生产种类, 0, U8 |
| ProductLvTable | Lv | 1.0 | 58 | 等级, 0, U8 |
| ProductLvTable | Exp | 1.0 | 240 | 下个熟练度, 1, S64 |
| ProductLvTable | TotalExp | 1.0 | 438 | 总熟练度经验值, 1, S64 |
| ProductLvTable | Comment | 1.0 | 443 | 企划者用, 0, CBwString |
| QuestCinemaTable | TID | 1.0 | 193 | 寻宝电影, 2, U32 |
| QuestCinemaTable | Skip | 0.9948 | 3 |  逃脱可能性（0：可能 -1：不可能）, U8, 0 |
| QuestCinemaTable | LimitTime | 0.9948 | 3 | 自动翻页时长（秒）, U8, 10 |
| QuestCinemaTable | BGM | 0.9897 | 2 | CBwString, Sound/BGM/BGM_02.ogg |
| QuestCinemaTable | SceneTID | 0.9948 | 193 | 注册名, U32:v, 400004|400005 |
| QuestCinemaTable | Comment | 0.0103 | 2 | 管理者, CBwString |
| QuestDropTable | TID | 0.9987 | 797 | Ыїв§, U32, 1 |
| QuestDropTable | Comment | 0.0025 | 2 | ЙмРэеп, CBwString |
| QuestDropTable | QuestTID | 0.9987 | 657 | ЬНОПIDеЫКХ, U32, 1 |
| QuestDropTable | NpcTID | 0.9987 | 593 | NpcЫїв§, U32, 501 |
| QuestDropTable | ItemTID | 0.9987 | 641 | ЯюФП, U32, 20155 |
| QuestDropTable | DropRate | 0.9987 | 4 | ЖЊЪЇТЪ, U32, 9000 |
| QuestDropTable | DropStack | 0.9987 | 3 | ЖЊЪЇТЪзюДѓЪ§, U32, 1 |
| QuestDropTable | DropAll | 0.9987 | 3 | бчЛсзДЬЌЪЧЪЧЗёжЇИЖ, U8, 1 |
| QuestMissionTable | TID | 0.9997 | 3819 | 索引, U32, 1 |
| QuestMissionTable | EngTitle | 0.972 | 3713 | 英文 目标, CBwString, QMT_Title_000001 |
| QuestMissionTable | EngPurpose | 0.972 | 3713 | 英文 提示, CBwString, QMT_Purpose_000001 |
| QuestMissionTable | LocalTitle | 0.9997 | 3294 | 韩语 目标, CBwString, 击杀哥布林后，收集掉落的可疑石雕塑。 |
| QuestMissionTable | LocalPurpose | 0.9997 | 3104 | 韩语 提示, CBwString, 石雕收集 |
| QuestMissionTable | Type | 0.9997 | 15 | 类型名称 1:狩猎(使用中) 2:对话(使用中) 3:项目收集(使用中) 4:项目使用(使用中) 5:护卫(使用中) 6:pvp 7:传达使用) 8:操作10：隐访问, U8, 3 |
| QuestMissionTable | Value | 0.9987 | 3006 | Type不同而不同, U32, 20155 |
| QuestMissionTable | Value2 | 0.9997 | 7 | Type不同而不同, U32, 0 |
| QuestMissionTable | Count | 0.9997 | 27 | 任务数, U32, 2 |
| QuestMissionTable | RemoveItem | 0.9997 | 4 | 项目删除, U8, 1 |
| QuestMissionTable | WorldTID | 0.9995 | 66 | U16, 2000, 2500 |
| QuestMissionTable | MapXYZ | 0.9806 | 1987 | 怪兽属性, F32:v, 1689.95|4741.98|71.50 |
| QuestRewardTable | TID | 0.9998 | 5382 | РЮЕІНК, U32, 100001 |
| QuestRewardTable | Type | 0.9998 | 5 | ХИРдИэФЊ 1:ОЦРЬХл 2:АжЕх 3:АцЧшФЁ 4:НКХШЦїРЮЦЎ 5:ЗЙКЇ 6:ЙЋБтАцЧшФЁ 7:ЙЋБтНКХГЦїРЮЦЎ 8:ЙЋБтЗЙКЇ 9:ШЃФЊ, U8, 3 |
| QuestRewardTable | Value | 0.9996 | 1087 | U32, 0, 2120001 |
| QuestRewardTable | Count | 0.9996 | 1254 | U32, 4200, 2700 |
| QuestRewardTable | IsSelect | 0.9998 | 4 | МБХУПЉКЮ 0:БтКЛ 1:МБХУ, U8, 0 |
| QuestSceneTable | TID | 1.0 | 571 | 任务场景, 2, U32 |
| QuestSceneTable | Comment | 0.0035 | 2 | 管理者, CBwString |
| QuestSceneTable | Type | 0.9983 | 5 | 类型 : 0 - 游戏画面, 1 - 2D画面, 2 - 视频, U8, 0 |
| QuestSceneTable | Movie | 0.0052 | 3 | 视频, CBwString, Movie\Intro.avi |
| QuestSceneTable | Image | 0.0052 | 3 | 照片, CBwString, UI\Texture\SB_BtnAimHighSelected.png |
| QuestSceneTable | Camera | 0.9983 | 4 | 探秘照相机, CBwString, quest_cam_alone_chest_buff |
| QuestSceneTable | TargetTID | 0.9983 | 67 | 相机焦点(0 - 播放), U32, 1009 |
| QuestSceneTable | EngDesc | 0.9983 | 571 | 英文 台词, CBwString, QST_Desc_000001 |
| QuestSceneTable | LocalDesc | 0.9983 | 570 | 韩文台词, CBwString, 最近 这一地区的恶魔发生过度增殖 |
| QuestSceneTable | Unnamed: 9 | 0.0 | 0 |  |
| QuestSceneTable | Unnamed: 10 | 0.0 | 0 |  |
| QuestSceneTable | Unnamed: 11 | 0.0 | 0 |  |
| QuestSceneTable | Unnamed: 12 | 0.0 | 0 |  |
| QuestSceneTable | Unnamed: 13 | 0.0 | 0 |  |
| QuestSceneTable | Unnamed: 14 | 0.0 | 0 |  |
| QuestSceneTable | Unnamed: 15 | 0.0 | 0 |  |
| QuestTable | TID | 0.9997 | 3278 | 指数：任务分离器, U32, 1 |
| QuestTable | Type | 0.9997 | 6 | 类型0：方案1：一般2：重复, U8, 0 |
| QuestTable | EngTitle | 0.9713 | 3185 | 英文 题目, CBwString, QUT_Title_000001 |
| QuestTable | EngMainScript | 0.9713 | 3185 | 英文 本文, CBwString, QUT_Main_000001 |
| QuestTable | EngProgressScript | 0.9713 | 3185 | 英文 进行中的npc 台词（详细信息显示在NPC????）, CBwString, QUT_Progress_000001 |
| QuestTable | EngFinishScript | 0.9713 | 3185 | 英语完成脚本, CBwString, QUT_Finish_000001 |
| QuestTable | EngMiniBarFinish | 0.9713 | 3185 | 英文 任务完成时 任务中出现的脚本, CBwString, QUT_Mini_000001 |
| QuestTable | LocalTitle | 0.9997 | 2949 | 韩语 字幕, CBwString, 哥布林的异常繁殖 |
| QuestTable | LocalMainScript | 0.9994 | 2307 | 中文 本文, CBwString, 最近.这个领域的哥布林正在异常繁殖. /n /n自然情况下是很少出现的状况，因此要镇压叛军平定这种状况. 但是围剿这些家伙们的话是否可以稳住这次事态? /n /n感觉这次异常繁殖现象不是自然性的现象. 所以 <TC '163:21:21' Text'在哥布林阵营' /><TC '163:21:21' Text'请干掉哥布林' />然后调查他们的尸体. |
| QuestTable | LocalProgressScript | 0.9991 | 2655 | 中文进行中的npc 台词（详细信息显示在NPC????）, CBwString, <TC '163:21:21' Text干掉'哥布林' />调查他们的尸体. |
| QuestTable | LocalFinishScript | 0.9985 | 2929 | 中文 完成脚本, CBwString, 带着的奇怪石雕还没有微弱,仍然感受到了黑暗气息. |
| QuestTable | LocalMiniBarFinish | 0.9997 | 887 | 中文任务完成时 任务中出现的脚本, CBwString, 艾丽卡传达石雕. |
| QuestTable | Area | 0.9997 | 27 | 地区, U32, 1102 |
| QuestTable | Grade | 0.9997 | 7 | 等级：1级：简单的2：有些简单的3：4平均：5的一些困难：硬盘, U8, 0 |
| QuestTable | Level | 0.9997 | 58 | 等级（在此适当的水平，以显示任务内容）, U8, 1 |
| QuestTable | Repeat | 0.9997 | 5 | 是否重复0：NR1：重复, U8, 0 |
| QuestTable | RepeatDay | 0.9997 | 4 | 重复单位, U32, 0 |
| QuestTable | Share | 0.9997 | 4 | 是否分享0:不分享 1:分享, U8, 1 |
| QuestTable | StartType | 0.9997 | 4 | 启动条件1：NPC接受2：自动主武器等级：项目采用3：本地访问车手4：questcomplete自动5：自动6人物等级, U8, 1 |
| QuestTable | StartValue | 0.9976 | 693 | 启动条件值, U32, 1009 |
| QuestTable | StartCinemaTID | 0.9997 | 25 | 开始电影导演, U32, 0 |
| QuestTable | FinishType | 0.9997 | 3 | 完成条件1：NPC完成2：自动完成, U8, 1 |
| QuestTable | FinishValue | 0.9976 | 654 | 完成条件值, U32, 1009 |
| QuestTable | FinishCinemaTID | 0.9994 | 3 | 整条生产电影, U32, 0 |
| QuestTable | TimeOut | 0.9994 | 3 | 时间限制（秒）, U32, 0 |
| QuestTable | PrevQuest | 0.9997 | 1445 | 上一个任务, U32:v, 0 |
| QuestTable | NextQuest | 0.9994 | 1113 | 下一个任务, U32:v, 3 |
| QuestTable | DemandRace | 0.9997 | 8 | 需要满足, U8:v, 1 |
| QuestTable | DemandLowLv | 0.9997 | 58 | 需要的最低水平, U8, 1 |
| QuestTable | DemandMaxLv | 0.9997 | 30 | 需要的最高水平, U8, 99 |
| QuestTable | DemandWeapon | 0.9997 | 3 | 要求主武器, U32:v, 0 |
| QuestTable | DemandWLv | 0.9997 | 3 | 所需的主要武器技能, U8:v, 0 |
| QuestTable | GiveItem1 | 0.9991 | 487 | 付款项目1, U32, 0 |
| QuestTable | GiveItemCnt1 | 0.9994 | 5 | 付款项目数量, U8, 0 |
| QuestTable | GiveItem2 | 0.9997 | 13 | 付款项目2, U32, 0 |
| QuestTable | GiveItemCnt2 | 0.9982 | 5 | 付款项目数量, U8, 0 |
| QuestTable | EventTID | 0.9997 | 3 | 事件发生 - 如果护送WORLDPLACE TID, U64, 0 |
| QuestTable | MissionTID | 0.9997 | 3278 | 使命阵列ID, U32:v, 1 |
| QuestTable | RewardTID | 0.9997 | 2888 | 焊惑酒捞叼硅凯, U32:v, 100001 |
| QuestTable | DropTID | 0.9997 | 544 | 降阵列, U32:v, 1 |
| RandomNodeTable | CharName | 1.0 | 5 | ČËÎďNIFĐŐĂű, 2, CBwString |
| RandomNodeTable | NodeName | 1.0 | 89 | ˝ÚµăĂűłĆ, 2, CBwString |
| SaleTable | TID | 0.9998 | 4446 | 区分者, U16, 1 |
| SaleTable | Comment | 0.9998 | 1721 | 企划自用, CBwString, 最低级精灵石柔性书(武器) |
| SaleTable | SaleTID | 0.9998 | 119 | 参考 TID, U8, 1 |
| SaleTable | slot | 0.9998 | 110 | 插槽号码, U8, 0 |
| SaleTable | ItemTID | 0.9998 | 3637 | 项目编号, U32, 41000 |
| SaleTable | ItemMaxSale | 0.9998 | 3 | 最大销售数量, U16, 0 |
| SaleTable | ItemMaxBuy | 0.9998 | 4 | 最大可能的购买数量, U16, 0 |
| SaleTable | SaleDay_01 | 0.9998 | 3 | 01#销售日期, U8, 8 |
| SaleTable | SaleStart_01 | 0.9998 | 3 | 01#销售开始时间, U8, 0 |
| SaleTable | SaleEnd_01 | 0.9998 | 3 | 01#销售结束日期, U8, 0 |
| SaleTable | SaleDay_02 | 0.9998 | 3 | 02#销售日期, U8, 8 |
| SaleTable | SaleStart_02 | 0.9998 | 3 | 02#销售开始时间, U8, 0 |
| SaleTable | SaleEnd_02 | 0.9998 | 3 | 02#销售结束时间, U8, 0 |
| ServerInfoTable | TID | 1.0 | 16 | 服务器号, 1, U32 |
| ServerInfoTable | Comment | 0.125 | 2 | 企划者用, CBwString |
| ServerInfoTable | ServerName | 0.9375 | 15 | 服务器名, CBwString, TestServer1 |
| ServerInfoTable | StateFlag | 0.9375 | 3 | 服务器状态(0: 一般, 2: 新, 4: 17代, 32: 推荐), U16, 0 |
| ServerInfoTable | LoginQueue | 0.9375 | 4 | 队列中人数, U32, 3000 |
| ServerInfoTable | PCMax | 0.9375 | 4 | PC 最大个数值, U64, 10240 |
| ServerInfoTable | NpcMax | 0.9375 | 4 | NPC 最大个数值, U64, 50000 |
| ServerInfoTable | EntityMax | 0.9375 | 3 | Entity 最大个数值, U64, 10000 |
| ServerInfoTable | SummonMax | 0.9375 | 3 | Summon 最大个数值, U64, 1024 |
| ServerInfoTable | ObjectMax | 0.9375 | 3 | Object 最大个数值, U64, 10000000 |
| SkillBaseAttackTable | TID | 1.0 | 12 |  롸잼포, 2, U8 |
| SkillBaseAttackTable | WeaponKind | 1.0 | 12 | 嶠포롸썩, 2, U8 |
| SkillBaseAttackTable | SkillTID | 1.0 | 13 | 세콘뵀쯤, 2, U32:v |
| SkillBaseAttackTable | CriticalSkillTID | 1.0 | 13 | 寮세콘뵀쯤, 2, U32:v |
| SkillComboTable | TID | 0.9744 | 38 | 人物, U16, 1 |
| SkillComboTable | ComboSkillGroup_0 | 0.9744 | 38 | 1阶段 连接技能, U32, 2 |
| SkillComboTable | ComboSkillGroup_1 | 0.9744 | 38 | 2阶段 连接技能, U32, 6 |
| SkillComboTable | ComboSkillGroup_2 | 0.9744 | 33 | 3阶段 连接技能, U32, 13 |
| SkillComboTable | ComboSkillGroup_3 | 0.9744 | 3 | 4阶段 连接技能, U32, 0 |
| SkillComboTable | ComboSkillGroup_4 | 0.9744 | 3 | 5阶段 连接技能, U32, 0 |
| SkillComboTable | MinComboSkillTime_0 | 0.9744 | 3 | 1阶段 技能 最小 输入时间, U32, 0 |
| SkillComboTable | MinComboSkillTime_1 | 0.9744 | 3 | 2阶段 技能 最小 输入时间, U32, 0 |
| SkillComboTable | MinComboSkillTime_2 | 0.9744 | 3 | 3阶段 最小 输入时间, U32, 0 |
| SkillComboTable | MinComboSkillTime_3 | 0.9744 | 3 | 4阶段 最小 输入时间, U32, 0 |
| SkillComboTable | MinComboSkillTime_4 | 0.9744 | 3 | 5阶段 最小 输入时间, U32, 0 |
| SkillComboTable | MaxComboSkillTime_0 | 0.9744 | 3 | 1阶段 最大输入时间, U32, 0 |
| SkillComboTable | MaxComboSkillTime_1 | 0.9744 | 4 | 2阶段 最大输入时间, U32, 5000 |
| SkillComboTable | MaxComboSkillTime_2 | 0.9744 | 4 | 3阶段 最大输入时间, U32, 5000 |
| SkillComboTable | MaxComboSkillTime_3 | 0.9487 | 3 | 4阶段 最大输入时间, U32, 0 |
| SkillComboTable | MaxComboSkillTime_4 | 0.9487 | 3 | 5阶段 最大输入时间, U32, 0 |
| SkillLearnTable | TID | 0.9972 | 362 | 核心价值, U16, 1 |
| SkillLearnTable | Comment | 0.9972 | 347 | 企划自用, CBwString, 矛的基本攻击 |
| SkillLearnTable | WeaponType | 0.9972 | 12 | 武器区分, U8, 1 |
| SkillLearnTable | SkillTID | 0.9972 | 362 | 技能编号, U32, 1 |
| SkillLearnTable | DX2 | 0.9972 | 10 | 技能形象 X坐标, U32, 111 |
| SkillLearnTable | DY2 | 0.9972 | 9 | 技能形象 Y坐标, U32, 22 |
| SkillLearnTable | NextTID | 0.0055 | 2 | 箭符号贴的 TID 编号, U16 |
| SkillTable | TID | 0.9999 | 11328 | 技能索引, U32, 1 |
| SkillTable | SkillGroup | 0.9999 | 2781 | 技能组合, U16, 0 |
| SkillTable | SkillLevel | 0.9999 | 12 | 技能等级, U8, 1 |
| SkillTable | Comment | 0.8237 | 3804 | 企划者用, CBwString, 1连击 1技能 |
| SkillTable | EngName | 0.9582 | 10855 | 英文名, CBwString, SKT_Name_000001 |
| SkillTable | LocalName | 0.9998 | 3010 | 名字, CBwString, 长枪基本攻击 |
| SkillTable | LearnType | 0.9999 | 6 | 使用类型, U8, 1 |
| SkillTable | Type | 0.9999 | 7 | 类型, U8, 1 |
| SkillTable | Kind | 0.9999 | 20 | 种类, U8, 0 |
| SkillTable | Property | 0.9999 | 18 | 属性, U8, 0 |
| SkillTable | BuffPosition | 0.9999 | 6 | buff种类, U8, 0 |
| SkillTable | BuffDelete | 0.9999 | 5 | buff解除 有/无, U8, 0 |
| SkillTable | InputType | 0.9999 | 7 | 使用方法, U8, 2 |
| SkillTable | Target | 0.9999 | 15 | 作用对象, U8, 20 |
| SkillTable | MaxArea_01 | 0.9999 | 29 | 圆形范围, U8:a:MaxArea, 0 |
| SkillTable | MaxArea_02 | 0.9999 | 19 | 直线型道路, U8, 0 |
| SkillTable | VolumeArea | 0.9999 | 12 | 适用对象数, U8, 1 |
| SkillTable | MinRange | 0.9999 | 6 | 最小攻击距离, U16, 0 |
| SkillTable | MaxRange | 0.9999 | 22 | 最广域攻击距离, U16, 3 |
| SkillTable | AutoLearnSkillTID | 0.9999 | 13 | 自动学习技能, U32, 0 |
| SkillTable | ComboSkillGroup | 0.9999 | 39 | 连接技能参考 TID, U16, 0 |
| SkillTable | ReqHP | 0.9999 | 3 | 消耗HP, U16, 0 |
| SkillTable | ReqMP | 0.9999 | 243 | 消耗MP, U16, 0 |
| SkillTable | NumericalClass | 0.9999 | 4 | %有/无, U8, 1 |
| SkillTable | KindValue | 0.9999 | 1023 | 属性值, U32, 0 |
| SkillTable | SuccessRate | 0.9999 | 8 | 成功率, U8, 100 |
| SkillTable | AddDamage | 0.9999 | 84 | 增加, U16, 0 |
| SkillTable | AgroValue | 0.9999 | 96 | 霸巨大值, F32, 10 |
| SkillTable |  AffectType | 0.9999 | 5 | 效果类型, U8, 0 |
| SkillTable |  AffectDuration | 0.9999 | 46 | 持续时间/周期效应, S64, 0 |
| SkillTable |  AffectCount | 0.9999 | 11 | 效果触发次数, U8, 0 |
| SkillTable | CoolTime | 0.9999 | 273 | 冷却时间, U32, 700 |
| SkillTable | GlobalCoolTime | 0.9999 | 20 | 全球冷却时间, U16, 0 |
| SkillTable | NextSkillTID | 0.9999 | 38 | 额外发生技能, U32, 0 |
| SkillTable | AddtionSkillTID | 0.9999 | 1265 | 追加效果号码, U32:v, 0 |
| SkillTable | AddtionRate | 0.9999 | 26 | 应用概率增加效果, U8:v, 0 |
| SkillTable | ReqItemTID | 0.9999 | 7 | 技能需要的道具 TID, U32, 0 |
| SkillTable | ReqItemTIDCount | 0.9999 | 4 | 技能需要的道具数量, U8, 0 |
| SkillTable | CastMoveAbility | 0.9999 | 6 | 可能移动 有/无, U8, 0 |
| SkillTable | CastingAniID | 0.9999 | 22 | 角色动画号码, U16, 0 |
| SkillTable | UpCastingAniID | 0.9999 | 3 | 上半身角色动画号码, U16, 0 |
| SkillTable | CastingTime | 0.9999 | 28 | 选定时间, U32, 0 |
| SkillTable | CastingFailRate | 0.9999 | 7 | 选定失败概率, U8, 0 |
| SkillTable | CastingDelayTime | 0.9999 | 3 | 角色延迟时间(准备戴穆里申), U32, 0 |
| SkillTable | CastingDelayRate | 0.9999 | 3 | 角色延迟概率(准备戴穆里申), U8, 0 |
| SkillTable | Race | 0.9999 | 9 | 种族, U8:v, 2|4 |
| SkillTable | LimitWeapon | 0.9999 | 13 | 武器限制, U8, 1 |
| SkillTable | LimitMainWeapon | 0.9999 | 13 | 主武器限制, U8, 0 |
| SkillTable | LimitWeaponLevel | 0.9999 | 3 | 武器熟练度等级限制, U8, 0 |
| SkillTable | OpenPoint | 0.4251 | 8 | 技能开放点, U16, 0 |
| SkillTable | LimitCharLevel | 0.9999 | 4 | 角色等级限制, U8, 0 |
| SkillTable | LearnSkillPoint | 0.9999 | 4 | 学习技能点, U8, 0 |
| SkillTable | PreConditionTID_01 | 0.9999 | 323 | 01#先行技能TID, U32, 0 |
| SkillTable | PreConditionTID_02 | 0.9999 | 3 | 02#先行技能TID, U32, 0 |
| SkillTable | SkillArea | 0.9999 | 4 | 能使用技能的地区, U8, 2 |
| SkillTable | NowGrade | 0.9999 | 8 | 现阶段, U8, 1 |
| SkillTable | MaxGrade | 0.9999 | 5 | 最广域阶段, U8, 1 |
| SkillTable | AniID | 0.9999 | 225 | 动作角色ID, U16:v, 1030|1031 |
| SkillTable | AniTime | 0.9999 | 114 | 动作时间, U32, 1400 |
| SkillTable | UpAniID | 0.9999 | 91 | 人物上半身ID, U16:v, 1032|1033 |
| SkillTable | UpAniTime | 0.9999 | 33 | 上半身时间, U32, 1400 |
| SkillTable | EnableMoving | 0.9999 | 4 | 是否移动攻击, U8, 1 |
| SkillTable | EffectiveRange | 0.9999 | 5 | 攻击距离, U16, 0 |
| SkillTable | AutoAttack | 0.9999 | 4 | 是否自动攻击, U8, 1 |
| SkillTable | ActionEffectname | 0.9999 | 982 | 动作效果名, CBwString:v, 01_030_001|01_031_001 |
| SkillTable | CameraID | 0.9999 | 3 | 指导摄影, U16, 0 |
| SkillTable | SkillIconID | 0.9999 | 505 | 技能图标, U16, 1 |
| SkillTable | EngDesc | 0.9942 | 10856 | 英文说明, CBwString, SKT_Desc_000001 |
| SkillTable | LocalDesc | 0.5733 | 2962 | 韩文说明, CBwString, <TC '240:163:63' Text'长枪基本攻击'/> |
| SkillTable | AlarmMsg | 0.0239 | 82 | NPC 活动消息, CBwString, ARMMSG_1044_01 |
| StatTable | TID | 0.9995 | 2006 | 索引(种族区分), U16, 0 |
| StatTable | StatClass | 0.9995 | 503 | 统计登记, U16, 0 |
| StatTable | StatPoint | 0.9995 | 4 | 需要点数, U8, 0 |
| StatTable | StrPOPMin | 0.9995 | 503 | 力量统计 - 最小物理攻击力, U16, 0 |
| StatTable | StrPOPMax | 0.9995 | 503 | 力量统计 - 最大物理攻击力, U16, 0 |
| StatTable | ConMaxHp | 0.9995 | 503 | 体力统计 - 最大生命值, U16, 0 |
| StatTable | ConHPR | 0.9995 | 503 | 体力统计 - HP 恢复, U16, 0 |
| StatTable | WisMOPMin | 0.9995 | 503 | 智力统计 - 最小魔法攻击力, U16, 0 |
| StatTable | WisMOPMax | 0.9995 | 503 | 智力统计 - 最大魔法攻击力, U16, 0 |
| StatTable | MenMaxMp | 0.9995 | 503 | 智能统计 - 最大魔法量, U16, 0 |
| StatTable | MenMPR | 0.9995 | 503 | 智能统计 - MP恢复, U16, 0 |
| StatTable | AgilityDP | 0.9995 | 503 | 敏捷 - 回避度, U16, 0 |
| StatTable | AgilityAP | 0.9995 | 328 | 敏捷 - 命中度, U16, 0 |
| StatTable | AgilityCP | 0.9995 | 463 | 敏捷 - 致命度, U16, 0 |
| SummonTable | TID | 0.9977 | 430 | 人物, U32, 1 |
| SummonTable | Comment | 0.1671 | 46 | 企划者用, CBwString, 咒术师帕朗突然地攻击（9029）使用技能“狼来了” |
| SummonTable | NPCTID | 0.9977 | 428 | NPC号码, U32, 300001 |
| SummonTable | AiTID | 0.0046 | 2 | AIDB_AttributesRecord, U32 |
| SummonTable | GoalTID | 0.0046 | 2 | AIDB_GoalSetRecord, U32 |
| SummonTable | Time | 0.9977 | 20 | 召唤时间, U32, 30000 |
| SummonTable | AreaTID | 0.9814 | 3 | 召唤坐标, U32, 0 |
| SummonTable | AS | 0.0046 | 2 | 攻击速度, U16 |
| SummonTable | RS | 0.0046 | 2 | 移动速度, U16 |
| TerrainSurfaceTable | TID | 0.9947 | 186 | 2, U32, 1 |
| TerrainSurfaceTable | Name | 0.9894 | 184 | string, Aimhigh_Brick_A, Aimhigh_Brick_F |
| TerrainSurfaceTable | FootSound_L | 0.9894 | 23 | string, Foot_Stone_01.ogg, Foot_Stone_03.ogg |
| TerrainSurfaceTable | FootSound_R | 0.9894 | 23 | string, Foot_Stone_02.ogg, Foot_Stone_04.ogg |
| TerrainSurfaceTable | FootSound_Up | 0.9894 | 3 | string, PC_Jump_00.ogg, PC_Land_Water_03.ogg |
| TerrainSurfaceTable | FootSound_Down | 0.9894 | 39 | string, PC_Land_Stone_01.ogg, PC_Land_Stone_02.ogg |
| TerrainSurfaceTable | FootEffect_L | 0.9894 | 10 | CBwString, FX_Brick_A, FX_grass_A |
| TerrainSurfaceTable | FootEffect_R | 0.9894 | 11 | CBwString, FX_Brick_A, FX_grass_A |
| TerrainSurfaceTable | FootEffect_Up | 0.0106 | 2 | CBwString, FX_river_a |
| TerrainSurfaceTable | FootEffect_Down | 0.9894 | 11 | CBwString, FX_Brick_A, FX_grass_A |
| TerrainSurfaceTable | Desc | 0.0957 | 18 | string, │Ū_│Ū╩ą╩»═Ę║ė┤▓, ę╗░ŃŲĘ |
| TipTable | TID | 1.0 | 104 | 区分, 2, U16 |
| TipTable | Type | 0.9905 | 4 | 1情况时加载画面上的输出提示, U8, 1 |
| TipTable | EngDesc | 0.9619 | 101 | 英文提示输出内容, CBwString, TPT_Desc_000001 |
| TipTable | LocalDesc | 0.9905 | 98 | 韩文提示输出内容, CBwString, <TC'255:255:0' Text'帮助语 :'/>任务目标在屏幕右侧/点击任务进行情况将会移动至任务目标区域。 |
| TitleTable | TID | 0.8333 | 5 | 指数:主区分, U16, 1 |
| TitleTable | EngName | 0.3333 | 2 | 英文名, CBwString |
| TitleTable | LocalName | 0.8333 | 5 | 韩文名, CBwString, 僵尸猎人 |
| TitleTable | FinishCount | 0.8333 | 4 | 完成达到的次数, U16, 100 |
| ToolWeaponTable | TID | 1.0 | 16 | 分离, 3, U16 |
| ToolWeaponTable | Name | 0.9375 | 15 | 名称, CBwString, 矛 |
| ToolWeaponTable | LeftMesh | 0.625 | 10 | 日期信息, CBwString, p_w_shle_04_lft_lod.nif |
| ToolWeaponTable | RightMesh | 0.75 | 12 | 日期信息, CBwString, p_w_lanc_04_all_lod.nif |
| TriggerTable | TID | 0.9971 | 346 | 模式号码, U32, 1 |
| TriggerTable | Comment | 0.9971 | 332 | 企划者用, CBwString, 英雄战战开始时门开 |
| TriggerTable | Owner | 0.9971 | 330 | 条件对象, CBwString:v, Racewar|1 |
| TriggerTable | Trigger | 0.9971 | 12 | 条件, CBwString:v, OnStart |
| TriggerTable | Target | 0.9971 | 172 | 作用对象, CBwString:v, Entity|300010 |
| TriggerTable | Action | 0.9971 | 118 | 作用效果, CBwString:v, ChangeState|2 |
| TriggerTable | ConUnion | 0.9971 | 4 | 阵营条件, U8, 0 |
| TriggerTable | ConLevel | 0.9942 | 3 | 等级条件, U8, 0 |
| TriggerTable | ConQuest | 0.9971 | 3 | 要求条件, U32, 0 |
| TriggerTable | Loop | 0.9971 | 3 | 再动作, U8, 0 |
| TriggerTable | TriggerMessageTarget | 0.0663 | 4 | U8, 0, 1 |
| TriggerTable | TriggerMessage | 0.0663 | 6 | CBwString, TRIGGERMSG_RACEWAR_ASSASSIN_CLEARSCORE_A, TRIGGERMSG_RACEWAR_ASSASSIN_CLEARSCORE_D |
| TutorialTable | TID | 1.0 | 69 | 人物, 2, U16 |
| TutorialTable | Comment | 0.6667 | 46 | 企划者用, CBwString:v, 角色描述标签界面。人物信息窗口（快捷键C）的角色标签时的最初一次只显示。 |
| TutorialTable | Type | 0.9855 | 8 | 调整轴类型, U8, 0 |
| TutorialTable | Value | 0.9855 | 10 | 调整轴值, U32:v, 1 |
| TutorialTable | TitleMsg | 0.2609 | 18 | 调整轴项目, CBwString:v, WORD_JOIN_INTERFACE|WORD_JOIN_MOUSE|WORD_JOIN_KEY|WORD_JOIN_SPIN|WORD_JOIN_ZOOM |
| TutorialTable | TutorialMovie | 0.2609 | 18 | 调整轴动画, CBwString:v, Join_Interface.avi|Join_MOUSE_MOVE.avi|Join_KEY_MOVE.avi|Join_Spin.avi|Join_Zoom.avi |
| TutorialTable | ExplainMsg | 0.8986 | 62 | 调整轴说明, CBwString:v, MSG_JOIN1|MSG_JOIN2|MSG_JOIN3|MSG_JOIN4|MSG_JOIN5 |
| TutorialTable | ToolTip | 0.3478 | 24 | 工具提示, CBwString, WORD_JOIN_INTERFACE |
| TutorialTable | UIP | 0.7536 | 40 | UI, CBwString, Charainfo |
| TutorialTable | ParentControl | 0.7536 | 51 | 程序控制, CBwString, Mark_LvUp |
| TutorialTable | ChildControl | 0.6667 | 46 | 坐标的标准控件, CBwString, Ci_CampInput |
| TutorialTable | Offset | 0.7101 | 41 | 调整坐标, F32:v, 1 |
| WarContentsTable | TID | 0.9615 | 25 | 分隔符, U8, 1 |
| WarContentsTable | Comment | 0.0769 | 2 | 企划者用, CBwString |
| WarContentsTable | EngName | 0.9615 | 25 | 英文说明, CBwString, WCT_Name_000001 |
| WarContentsTable | LocalName | 0.9615 | 25 | 韩文说明, CBwString, 英雄战 |
| WarContentsTable | Type | 0.9615 | 4 | 战斗时间, U8, 1 |
| WarContentsTable | Kind | 0.9615 | 9 | 种类, U8, 2 |
| WarContentsTable | Goal | 0.9615 | 10 | 胜利目标, U16, 800 |
| WarContentsTable | MaxPerson | 0.9615 | 4 | 最大参战人数, U16, 200 |
| WarContentsTable | ReqMinLevel | 0.9615 | 7 | 入场最低等级, U8, 40 |
| WarContentsTable | ReqMaxLevel | 0.9615 | 6 | 入场最高等级, U8, 50 |
| WarContentsTable | ReqItem | 0.9615 | 4 | 需要物品, U32, 0 |
| WarContentsTable | ReqItemCount | 0.9615 | 4 | 需要物品数量, U8, 0 |
| WarContentsTable | OptionValue1 | 0.3462 | 4 | 优先值1, U32, 5 |
| WarContentsTable | OptionValue2 | 0.1538 | 4 | 优先值2, U32, 150 |
| WarContentsTable | OptionValue3 | 0.1538 | 4 | 优先值3, U32, 500 |
| WarContentsTable | OptionValue4 | 0.1538 | 4 | 优先值4, U32, 1500 |
| WarContentsTable | OptionValue5 | 0.1538 | 4 | 优先值5, U32, 10000 |
| WarContentsTable | StandbyTime | 0.9615 | 5 | 战场开始待机时间, U8, 5 |
| WarContentsTable | LimitTime | 0.9615 | 4 | 限制时间, U16, 20 |
| WarContentsTable | MapTID | 0.9615 | 25 | 地图号, U16, 1007 |
| WarContentsTable | StartDay | 0.9615 | 10 | 开始星期, U8, 3 |
| WarContentsTable | StartTime | 0.9615 | 5 | 开始时间, U8:v, 12|20|21|22|23 |
| WarContentsTable | FameKill | 0.9615 | 5 | 标定值(声望结算式), F32, 30 |
| WarContentsTable | MinContribution | 0.9615 | 4 | 最小贡献值, F32, 1 |
| WarContentsTable | Contribution | 0.9615 | 4 | 最终贡献点结算式, F32, 0.005 |
| WarContentsTable | RankFame | 0.9231 | 4 | 战场排名点数(1位~20位固定值), U16:v, 200|190|180|170|160|150|140|130|120|110|100|90|80|70|60|50|40|30|20|10 |
| WarContentsTable | GoalAchieve | 0.9615 | 9 | 战场目标达成点数, U16, 0 |
| WarContentsTable | FameWinPoint | 0.9615 | 4 | 胜利阵营声望奖励点数基本值, U16, 10 |
| WarContentsTable | FameLosePoint | 0.9615 | 4 | 失败阵营声望奖励点数基本值, U16, 5 |
| WarContentsTable | FameDrawPoint | 0.9615 | 4 | 无胜负阵营声望奖励点数基本值, U16, 0 |
| WarContentsTable | CampBuff | 0.9615 | 4 | 奖励阵营buff, U32, 230511 |
| WarContentsTable | WinCoin | 0.9615 | 4 | 胜利阵营金币, U8, 3 |
| WarContentsTable | LoseCoin | 0.9615 | 4 | 失败阵营金币, U8, 1 |
| WarContentsTable | DrawCoin | 0.9615 | 4 | 无胜负金币, U8, 1 |
| WarContentsTable | WinMail | 0.9615 | 16 | 胜利阵营通过邮件给予物品奖励, U32, 1000 |
| WarContentsTable | LoseMail | 0.9615 | 4 | 失败阵营通过邮件给予物品, U32, 1001 |
| WarContentsTable | DrawMail | 0.9615 | 4 | 无胜负阵营通过邮件给予物品, U32, 1002 |
| WarContentsTable | EngDesc | 0.9615 | 25 | 英文的使用方法, CBwString, WCT_Desc_000001 |
| WarContentsTable | LocalDesc | 0.9615 | 15 | 韩文的使用方法, CBwString, 首先到达kill目标的阵营获得战场胜利./n /n干掉对方阵营是kill目标的关键. |
| WarContentsTable | WarImg | 0.9615 | 10 | 战场图像, U16, 2 |
| WarUniformTable | TID | 1.0 | 6 | 种族, 2, U8 |
| WarUniformTable | Comment | 0.8571 | 6 | 企划者用, CBwString, 人类 |
| WarUniformTable | UniformItemID | 0.8571 | 4 | 条款 TID, U32, 401000 |
| WeaponAbilityTable | TID | 1.0 | 22 | 仓库钥匙价格, 1, U32 |
| WeaponAbilityTable | Group | 1.0 | 4 | 团队熟练度, 1, U16 |
| WeaponAbilityTable | Lv | 1.0 | 12 | 熟练度等级, 1, U8 |
| WeaponAbilityTable | POPMin | 1.0 | 12 | 最小物理攻击力, 1, U16 |
| WeaponAbilityTable | POPMax | 1.0 | 12 | 最大物理攻击力, 1, U16 |
| WeaponAbilityTable | MOPMin | 1.0 | 12 | 最小魔法攻击力, 1, U16 |
| WeaponAbilityTable | MOPMax | 1.0 | 12 | 最大魔法攻击力, 1, U16 |
| WeaponAbilityTable | AP | 1.0 | 12 | 命中率, 1, U8 |
| WeaponAbilityTable | CP | 1.0 | 12 | 知名度, 1, U8 |
| WeaponAbilityTable | AS | 1.0 | 12 | 攻击速度, 1, U8 |
| WeaponLvTable | TID | 1.0 | 1006 | 人物, 0, U16 |
| WeaponLvTable | Kind | 1.0 | 16 | 武器种类, 0, U8 |
| WeaponLvTable | Lv | 1.0 | 103 | 等级, 0, U8 |
| WeaponLvTable | Exp | 1.0 | 104 | 下个熟练度, 1, S64 |
| WeaponLvTable | TotalExp | 1.0 | 104 | 总熟练度经验值, 1, S64 |
| WeaponLvTable | MainSp | 0.999 | 4 | 主武器时添加相应的技能点, U16, 0 |
| WeaponLvTable | ResetMainSp | 0.999 | 102 | 主武器技能点重置, U16, 0 |
| WeaponLvTable | SubSp | 1.0 | 4 | 辅助武器技能点, 1, U16 |
| WeaponLvTable | ResetSubSp | 1.0 | 102 | 辅助武器技能重置积分, 1, U16 |
| WeaponLvTable | Comment | 1.0 | 1006 | 企划者用 用途说明, 2, CBwString |
| WeaponLvTable | Ghelld | 0.999 | 3 | 上升级别所需货币, U32, 0 |
| WeaponLvTable | HPRBuff | 0.999 | 3 | HP 追加回复量, S32, 0 |
| WeaponLvTable | MPRBuff | 0.999 | 3 | MP 追加回复量, S32, 0 |
| WeaponLvTable | POPMin | 0.999 | 207 | 最小物理攻击力, U16, 1 |
| WeaponLvTable | POPMax | 0.999 | 222 | 最大物理攻击力, U16, 2 |
| WeaponLvTable | MOPMin | 0.999 | 168 | 最小魔法攻击力, U16, 0 |
| WeaponLvTable | MOPMax | 0.999 | 174 | 最大魔法攻击力, U16, 0 |
| WeaponLvTable | IGN_AT | 0.999 | 3 | 无视防御攻击力, U16, 0 |
| WeaponLvTable | AP | 0.999 | 60 | 命中度, U8, 0 |
| WeaponLvTable | CP | 0.999 | 43 | 致命一击, U8, 0 |
| WeaponLvTable | BP | 0.999 | 36 | 拦截度, U8, 0 |
| WeaponLvTable | AS | 0.999 | 3 | 攻击速度, U16, 0 |
| WeaponLvTable | STR | 0.999 | 3 | 气力, U8, 0 |
| WeaponLvTable | CON | 0.999 | 3 | 体力, U8, 0 |
| WeaponLvTable | WIS | 0.999 | 3 | 智慧, U8, 0 |
| WeaponLvTable | MEN | 0.999 | 3 | 智力, U8, 0 |
| WeaponLvTable | AGI | 0.999 | 3 | 敏捷, U8, 0 |
| WeatherTable | TID | 0.9924 | 130 | 2, U32, 1000 |
| WeatherTable | Type | 0.9847 | 5 | U32, 0, 1 |
| WeatherTable | Name | 0.9847 | 117 | CBwString, default_midnight, default_dawn |
| WeatherTable | Attrib | 0.9847 | 125 | CBwString, RainAlpha|0|RainColor|15194057|RainDropAlpha|0|RainDropAniSpeed|1|RainPlaneCount|10|RainScaleH|1.2|RainScaleV|0.8|RainSoundFile1|Mute_Sound_02.ogg|RainSpeed|0.8|, RainAlpha|0|RainColor|16777088|RainDropAlpha|0|RainDropAniSpeed|1|RainPlaneCount|10|RainScaleH|1.2|RainScaleV|0.8|RainSoundFile1|Mute_Sound_02.ogg|RainSpeed|0.8| |
| WorldEnvLightTable | TID | 1.0 | 8976 | ЕЦЙт, 2, U32 |
| WorldEnvLightTable | WorldTID | 0.9999 | 72 | ЪРНч, U16, 1 |
| WorldEnvLightTable | Type | 0.9999 | 3 | ЕЦЙтжжРр, U8, 0 |
| WorldEnvLightTable | Name | 0.9999 | 8976 | УћГЦ, CBwString, LightPoint:0001 |
| WorldEnvLightTable | Pos | 0.9999 | 8969 | ЮЛжУ, F32:v, 146.878|24.633|12.310 |
| WorldEnvLightTable | Rotation | 0.9999 | 6 | а§зЊ, F32:v, 0.000|0.000|0.000 |
| WorldEnvLightTable | Ambient | 0.9999 | 6 | Ambient, F32:v, 255.000|255.000|255.000 |
| WorldEnvLightTable | Diffuse | 0.9999 | 127 | Diffuse, F32:v, 255.000|255.000|250.000 |
| WorldEnvLightTable | Specular | 0.9999 | 3 | Specular, F32:v, 255.000|255.000|255.000 |
| WorldEnvLightTable | Dimmer | 0.9999 | 34 | ЧПЖШ, F32, 1 |
| WorldEnvLightTable | Radius | 0.9999 | 58 | АыОЖ, F32, 10 |
| WorldEnvLightTable | SpotIn | 0.9999 | 4 | SpotIn, F32, 0 |
| WorldEnvLightTable | SpotOut | 0.9999 | 4 | SpotOut, F32, 0 |
| WorldEnvSoundTable | TID | 1.0 | 5197 | °йЧа, 2, U32 |
| WorldEnvSoundTable | WorldTID | 0.9998 | 67 | КАЅз, U16, 2000 |
| WorldEnvSoundTable | Name | 0.9998 | 56 | ГыіЖ, CBwString, Amb_Fire_Bonfire_01.ogg |
| WorldEnvSoundTable | Pos | 0.9998 | 4714 | О»ЦГ, F32:v, 7043.44|7886.51|96.20 |
| WorldEnvSoundTable | Min | 0.9998 | 36 | °лѕ¶, F32, 2 |
| WorldEnvSoundTable | Max | 0.9998 | 36 | ЧоРЎѕаАл, F32, 10 |
| WorldEnvSoundTable | Volume | 0.9998 | 4 | ЧоґуѕаАл, F32, 1 |
| WorldEnvSoundTable | Unnamed: 7 | 0.0002 | 1 | ТфБї |
| WorldEnvWaterTable | TID | 0.9722 | 34 | 2, U32, 0 |
| WorldEnvWaterTable | Name | 0.9722 | 35 | 2, CBwString, Bleedmeel_Farm |
| WorldEnvWaterTable | ShaderName | 0.9722 | 4 | 2, CBwString, A2WaterShader |
| WorldEnvWaterTable | ShaderAttrib | 0.9722 | 35 | 2, CBwString, WColor|277472|SColor|FFFFFF|WDeep|0.950000|RPower|0.450|WPower|0.000|WSize|1.000|WSpeed|0.040|WDir|0.270|Trens|0.790|WName|Texture/Terrain/Water/Waves.dds|RName|Texture/Terrain/Water/wreflection.dds| |
| WorldMapUITable | TID | 0.9938 | 159 | 之后进入物质界的话 2000, U32, 1000 |
| WorldMapUITable | Comment | 0.3125 | 16 | 企划者用, CBwString, 大城市 |
| WorldMapUITable | EngName | 0.9875 | 158 | 英文地域名, CBwString, WMT_Name_000001 |
| WorldMapUITable | LocalName | 0.9938 | 145 | 韩文地域名, CBwString, 坎德拉大陆 |
| WorldMapUITable | Type | 0.9875 | 5 | U8, 1, 2 |
| WorldMapUITable | WorldTID | 0.9875 | 143 | U16, 2000, 2500 |
| WorldMapUITable | ParentTID | 0.9875 | 5 | U32, 0, 1000 |
| WorldMapUITable | Map | 0.9688 | 62 | CBwString, Aimhigh_SteelBreath.png, Aimhigh_Lohengrin.png |
| WorldMapUITable | LoadingMap | 0.5875 | 40 | U32:v, 1004, 1005 |
| WorldMapUITable | TipTID | 0.5875 | 16 | U16:v, 161|162|163, 141|142|143 |
| WorldMapUITable | RoadMap | 0.9688 | 16 | CBwString:v, 0_0, 2_8|2_9|2_10|3_9|3_10 |
| WorldMapUITable | StartX | 0.9875 | 22 | F32, -5, -4 |
| WorldMapUITable | StartY | 0.9875 | 24 | F32, 9037, 5852 |
| WorldMapUITable | EndX | 0.9875 | 22 | F32, 9492, 4913 |
| WorldMapUITable | EndY | 0.9875 | 24 | F32, 2670, 2558 |
| WorldMapUITable | C1StartX | 0.9875 | 12 | F32, 0, 1025 |
| WorldMapUITable | C1StartY | 0.9875 | 13 | F32, 0, 512 |
| WorldMapUITable | C1EndX | 0.9875 | 14 | F32, 0, 512 |
| WorldMapUITable | C1EndY | 0.9875 | 11 | F32, 0, 4608 |
| WorldMapUITable | C2StartX | 0.1375 | 12 | F32, 0, 769 |
| WorldMapUITable | C2StartY | 0.1375 | 10 | F32, 0, 4608 |
| WorldMapUITable | C2EndX | 0.1375 | 11 | F32, 0, 1536 |
| WorldMapUITable | C2EndY | 0.1375 | 11 | F32, 0, 4097 |
| WorldMapUITable | C3StartX | 0.1375 | 3 | F32, 0, 1536 |
| WorldMapUITable | C3StartY | 0.1375 | 3 | F32, 0, 3585 |
| WorldMapUITable | C3EndX | 0.1375 | 3 | F32, 0, 2049 |
| WorldMapUITable | C3EndY | 0.1375 | 3 | F32, 0, 3073 |
| WorldPlaceTable | TID | 1.0 | 32298 | 即时, U32, 4 |
| WorldPlaceTable | WorldTID | 1.0 | 120 | 世界安排, U16, 2500 |
| WorldPlaceTable | PlaceType | 1.0 | 4 | PlaceType, U8, 2 |
| WorldPlaceTable | PlaceTypeTID | 1.0 | 4377 | PlaceTypeTID, U32, 200101 |
| WorldPlaceTable | Pos | 1.0 | 30853 | 位置, F32:v, 77.65|436.92|192.71 |
| WorldPlaceTable | Rotation | 1.0 | 537 | Z轴心旋转, F32, 3.08 |
| WorldPlaceTable | Radius | 1.0 | 3 | 半径, F32, 0 |
| WorldPlaceTable | GroupNpc | 1.0 | 1531 | NpcTable, U64, 0 |
| WorldPlaceTable | State | 1.0 | 16 | State, U32, 0 |
| WorldPlaceTable | WarView | 1.0 | 4 | WarView, U8, 0 |
| WorldPlaceTable | PatrolPos | 0.0261 | 730 | PatrolPos, F32:v, 1177.63|5534.41|67.94|1166.89|5532.69|66.27|1152.34|5525.76|63.29 |
| WorldTable | TID | 0.9881 | 166 | U16, 1, 2 |
| WorldTable | Type | 0.994 | 7 | 2= зжЖЮ, 4= МДЪБ, 6= ДѓЙцФЃеНГЁ, 7= аЁЙцФЃеНГЁ, U32, 0 |
| WorldTable | LoadType | 0.994 | 4 | 0 = Seamless, 1 = Zone, U8, 1 |
| WorldTable | ContentsLimit | 0.994 | 7 | 1 =ВЛдЪаэзјЦя , 2 = PVPВЛФм 4 = ВЛПЩНЛвз  8 = ЮоИіЬхЩЬЕъ, U32, 3 |
| WorldTable | Name | 0.994 | 167 | 1=ЙВЭЌ(ШЫЮябЁдёЕШ).1000=еНГЁ.2000=ЪРНч.3000=ЕиЯТГЧ.4000=МДЪБ.5000=ЯажУ.10000=ВтЪд.ШЫЮяЙЄОп, CBwString, ШЫЮяЩњГЩ(ИпМЖ) |
| WorldTable | EngName | 0.9643 | 52 | CBwString, CreateAimhigh, CreateDemolition |
| WorldTable | Channel | 0.994 | 4 | ЦЕЕР, U8, 0 |
| WorldTable | MapX | 0.994 | 5 | КсЯђИіЪ§, U16, 1 |
| WorldTable | MapY | 0.994 | 5 | ЪњЯђИіЪ§, U16, 1 |
| WorldTable | MapSizeX | 0.994 | 5 | ЕиЭМПэЖШ, U16, 256 |
| WorldTable | MapSizeY | 0.994 | 5 | ЕиЭМПэЖШ, U16, 256 |
| WorldTable | WorldProperty | 0.994 | 85 | ЙВЭЌЪЙгУЕФЛЗОГжЕ(Йт, ЛЗОГвєРж, ДЩЪєад, аЁЕиЭМ), U16, 1 |
| WorldTable | RebirthTime | 0.994 | 6 | ИДЛюЪБМф, U32, 0 |
| WorldTable | Human_Pos | 0.994 | 59 | 1КХ ШЫРрЦ№Еу, F32:v, 0.00|0.00|0.00 |
| WorldTable | Human_Pos1 | 0.994 | 59 | 2КХ ШЫРрЦ№Еу, F32:v, 0.00|0.00|0.00 |
| WorldTable | Human_Pos2 | 0.994 | 59 | 3КХ ШЫРрЦ№Еу, F32:v, 0.00|0.00|0.00 |
| WorldTable | Human_Invasion | 0.0238 | 3 | ШЫРрГЧЪаНјЙЅзјБъжЕ, F32:v, 6798.03|7799.27|108.94|6798.03|7799.27|108.94|6798.03|7799.27|108.94|2014.11|4878.31|174.39|2014.11|4878.31|174.39|2014.11|4878.31|174.39 |
| WorldTable | Human_Radius | 0.9286 | 8 | ШЫРрПЊЪМАыОЖ, F32, 17 |
| WorldTable | MoonElf_Pos | 0.994 | 58 | 1КХ дТОЋСщЦ№Еу, F32:v, 0.00|0.00|0.00 |
| WorldTable | MoonElf_Pos1 | 0.994 | 58 | 2КХ дТОЋСщЦ№Еу, F32:v, 0.00|0.00|0.00 |
| WorldTable | MoonElf_Pos2 | 0.994 | 58 | 3КХ дТОЋСщЦ№Еу, F32:v, 0.00|0.00|0.00 |
| WorldTable | MoonElf_Invasion | 0.0179 | 3 | дТОЋСщГЧЪаНјЙЅзјБъжЕ, F32:v, 1770.83|4766.45|68.62|1770.83|4766.45|68.62|1770.83|4766.45|68.62|7039.83|7822.47|91.45|7039.83|7822.47|91.45|7039.83|7822.47|91.45 |
| WorldTable | MoonElf_Radius | 0.9286 | 8 | дТОЋСщЦ№Еу, F32, 17 |
| WorldTable | DragonScion_Pos | 0.994 | 58 | 1КХ СњжЎИДГ№епЦ№Еу, F32:v, 0.00|0.00|0.00 |
| WorldTable | DragonScion_Pos1 | 0.994 | 58 | 2КХ СњжЎИДГ№епЦ№Еу, F32:v, 0.00|0.00|0.00 |
| WorldTable | DragonScion_Pos2 | 0.994 | 58 | 3КХ СњжЎИДГ№епЦ№Еу, F32:v, 0.00|0.00|0.00 |
| WorldTable | DragonScion_Invasion | 0.0179 | 3 | СњжЎИДГ№епГЧЪаНјЙЅзјБъжЕ, F32:v, 7039.83|7822.47|91.45|7039.83|7822.47|91.45|7039.83|7822.47|91.45|1770.83|4766.45|68.62|1770.83|4766.45|68.62|1770.83|4766.45|68.62 |
| WorldTable | DragonScion_Radius | 0.9286 | 8 | СњжЎИДГ№епЦ№Еу, F32, 17 |
| WorldTable | Orc_Pos | 0.994 | 58 | 1КХ ЪозхЦ№Еу, F32:v, 0.00|0.00|0.00 |
| WorldTable | Orc_Pos1 | 0.994 | 58 | 2КХ ЪозхЦ№Еу, F32:v, 0.00|0.00|0.00 |
| WorldTable | Orc_Pos2 | 0.994 | 58 | 3КХ ЪозхЦ№Еу, F32:v, 0.00|0.00|0.00 |
| WorldTable | Orc_Invasion | 0.0238 | 3 | ЪозхГЧЪаНјЙЅзјБъжЕ, F32:v, 1990.31|5014.03|144.11|1990.31|5014.03|144.11|1990.31|5014.03|144.11|6797.80|7935.23|126.86|6797.80|7935.23|126.86|6797.80|7935.23|126.86 |
| WorldTable | Orc_Radius | 0.9286 | 8 | ЪозхЦ№Еу, F32, 17 |
| WorldTable | SunFilePath | 0.994 | 6 | ЬЋбєЗНЯђЮФМў, string, sun_ch_create.nif |
| WorldTable | Desc | 0.9881 | 15 | CBwString, ШЫЮяЩњГЩ, ШЫЮябЁдё |
