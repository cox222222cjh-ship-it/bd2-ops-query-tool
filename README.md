# 霸王大陆2 配置查询器

一个面向运营、策划、客服、测试的**只读型内部配置查询工具**。

本项目的目标不是在线改表，而是把 `data/current/` 下约 90 张配置表，逐步建设成一套**可检索、可追溯、可解释、可关联**的数据底座，并最终提供“按物品 / 任务 / 礼包 / 强化配置聚合查询”的网页工具。

---

## 1. 当前阶段目标

当前只做**第一阶段：数据底座与最小查询闭环**。

本阶段只完成以下工作：

1. 扫描 `data/current/` 下全部配置表
2. 自动识别文件编码、分隔符、字段结构、基础类型特征
3. 将全部表导入 SQLite
4. 生成 schema / 字段 / 枚举 / 候选关系索引
5. 输出候选业务域报告与待确认字段报告
6. 打通一条“按物品聚合查询”的最小闭环（命令行或简单 API）

本阶段**不做在线编辑，不写回原始表，不抢跑完整前端**。

---

## 2. 适合本项目的工作方式

### 推荐主模式
- Codex Web
- GitHub 私有仓库
- Codex Cloud Environments

### 原因
本项目属于：
- 表数量多
- 需要多轮扫描和重跑
- 依赖 Python / pandas / SQLite
- 很容易被本地 Windows 环境、路径、编码、依赖问题拖慢

因此，默认把 **云端可复现执行** 作为第一优先级，而不是要求本机先全部跑通。

### 本地工具的定位
本地 App / IDE / CLI 仅用于：
- 查看 diff
- 本地看网页效果
- 少量调试失败脚本
- 验证导出结果

---

## 3. 项目边界

### 明确做的事
- 读取、解析、索引配置表
- 统一导入 SQLite
- 提供跨表追溯与候选关联
- 输出字段字典草案、候选关系报告、异常清单
- 最终支持物品、强化、任务、礼包四大业务域聚合查询

### 明确不做的事
- 不修改原始表
- 不提供在线改表
- 不臆断字段语义
- 不把不确定关系写死为最终业务逻辑
- 不在第一阶段优先做完整 UI

---

## 4. 项目建议工具清单

### 必需工具
- Python 3.11+
- Git
- GitHub 私有仓库
- Codex Web

### 第一阶段核心库
- pandas
- sqlite3（Python 标准库）
- charset-normalizer
- PyYAML
- python-dateutil
- tabulate

### 第二阶段建议库
- FastAPI
- uvicorn
- pydantic
- SQLAlchemy（可选）

### 可选辅助工具
- DB Browser for SQLite（方便人工查看数据库）
- VS Code（只用于查看代码和结果，不作为主执行前提）
- Node.js 20+（仅第三阶段网页端需要）

---

## 5. 推荐仓库结构

```text
repo/
├─ AGENTS.md
├─ README.md
├─ requirements.txt
├─ data/
│  ├─ current/                 # 原始配置表，只读
│  ├─ cache/                   # 解析缓存、失败清单、schema
│  ├─ indexes/                 # 表/字段/关系/枚举索引
│  ├─ db/                      # SQLite 数据库
│  └─ snapshots/               # 手工备份
├─ rules/                      # 候选映射、人工确认规则
├─ scripts/                    # 扫描/导入/索引/验证脚本
├─ docs/                       # 扫描报告、字段字典、关系报告
├─ tests/                      # 脚本与规则校验
└─ api/                        # 第二阶段 API
```

---

## 6. 第一阶段必须产出的文件

### 数据文件
- `data/cache/tables_manifest.json`
- `data/cache/raw_schema.json`
- `data/cache/parse_failures.json`
- `data/db/config_tables.sqlite`
- `data/indexes/table_registry.json`
- `data/indexes/field_registry.json`
- `data/indexes/enum_profiles.json`
- `data/indexes/relation_candidates.json`
- `data/indexes/domain_candidates.json`

### 文档
- `docs/scan_summary.md`
- `docs/candidate_tables.md`
- `docs/candidate_relations.md`
- `docs/field_dictionary_draft.md`
- `docs/unknown_fields_todo.md`
- `docs/item_query_minimum_path.md`

---

## 7. 执行原则

1. 禁止用 PowerShell 做逐行表解析主逻辑
2. 表解析必须用 Python
3. 优先 pandas，必要时退回 `csv` 标准库
4. 原始表只读，不得改写 `data/current/`
5. 所有脚本必须可重复运行
6. 所有输出必须可追溯到原始文件名、字段名、行号或主键
7. 所有不确定结论必须显式标注“待确认”

---

## 8. 推荐实施顺序

### 第 1 步：建表清单
输出所有文件的：
- 文件名
- 编码
- 分隔符
- 表头
- 列数
- 行数
- 解析是否成功

### 第 2 步：统一导入 SQLite
每张表都落一份标准化表结构，并保留来源元信息。

### 第 3 步：生成索引
输出：
- 表索引
- 字段索引
- 枚举分布
- 主键候选
- 外键候选
- 候选业务域分类

### 第 4 步：生成报告
形成：
- 候选表报告
- 候选关系报告
- 字段字典草案
- 待确认字段清单

### 第 5 步：打通最小查询闭环
至少实现：
- 输入物品 ID / 名称
- 返回命中的主表记录
- 返回可能引用该物品的奖励、任务、礼包、强化相关记录
- 每条结果显示来源表名、字段名、原始值

---

## 9. 推荐脚本规划

建议逐步落这些脚本：

```text
scripts/
├─ scan_tables.py
├─ import_to_sqlite.py
├─ build_indexes.py
├─ detect_domains.py
├─ generate_reports.py
├─ query_item.py
└─ validate_outputs.py
```

说明：
- `scan_tables.py`：扫描全部表，识别结构并输出 manifest
- `import_to_sqlite.py`：导入 SQLite
- `build_indexes.py`：生成字段、枚举、候选关系索引
- `detect_domains.py`：识别物品 / 强化 / 任务 / 礼包候选表
- `generate_reports.py`：生成 docs 报告
- `query_item.py`：做最小可用查询链路
- `validate_outputs.py`：检查产物是否齐全、JSON 是否可读

---

## 10. 快速开始

### 1）创建虚拟环境
```bash
python -m venv .venv
source .venv/bin/activate
```

Windows PowerShell：
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2）安装依赖
```bash
pip install -r requirements.txt
```

### 3）准备目录
确保以下目录存在：
- `data/current/`
- `data/cache/`
- `data/indexes/`
- `data/db/`
- `docs/`
- `rules/`
- `scripts/`

### 4）按顺序执行
```bash
python scripts/scan_tables.py
python scripts/import_to_sqlite.py
python scripts/build_indexes.py
python scripts/detect_domains.py
python scripts/generate_reports.py
python scripts/query_item.py --keyword 测试物品
```

---

## 11. 验收标准

满足以下条件，视为第一阶段合格：

- 90 张左右表能稳定扫描
- 失败表能进入失败清单，而不是静默跳过
- SQLite 中可统一查询全部已成功解析表
- 能产出字段索引、枚举索引、候选关系索引
- 能输出待确认字段清单
- 输入一个物品时，至少能返回它在多张表中的关联信息
- 所有结果都能追溯到原始来源

---

## 12. 给 Codex 的首轮任务建议

把任务拆小，不要直接下“做完整系统”。

推荐首轮顺序：

1. 只创建目录结构和空脚本
2. 只实现 `scan_tables.py`
3. 扫描后生成 `tables_manifest.json` 和 `parse_failures.json`
4. 再实现 SQLite 导入
5. 再实现索引与报告
6. 最后再做最小查询接口

推荐首轮提示语：

```text
请严格遵守仓库根目录的 AGENTS.md。
先不要做前端。
先只完成第一阶段的数据底座。
第一步仅创建 scripts/、docs/、rules/、data/ 目录约定，并实现 scan_tables.py：
- 扫描 data/current/ 下所有表
- 自动识别编码、分隔符、列名、行数
- 输出 tables_manifest.json、raw_schema.json、parse_failures.json
- 不修改原始文件
- 所有不确定字段与异常都要保留
完成后只提交这一阶段所需的最小代码与文档。
```

---

## 13. 注意事项

- 没有完整客户端/服务端源码时，不要假装知道业务逻辑
- “像主键”“像外键”“像物品表”都只能先写成候选结论
- 表头短、字段名弱语义、值域不明确时，必须进入待确认清单
- 报告要让非程序同事也能看懂

---

## 14. 后续阶段

### 第二阶段
- 做 FastAPI 查询接口
- 封装物品 / 任务 / 礼包 / 强化聚合查询

### 第三阶段
- 做网页查询端
- 支持搜索、跳转、来源追溯、结果分组展示
- 必要时再接入截图/导出功能

在第二阶段未稳定前，不建议大规模投入网页视觉层开发。
