## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow inkludert)

Genererar ein XYZ-Gridplot frå ei liste over bilete.
Den tek ei liste over bilete (inkludert batchar) og flattar dei inn i ei lang liste først (derfor `batch_size=1`).

**Rutenettform**
Avgjer formen på rutenettet ved:
1. antalet radetikettar
2. antalet kolonnetikettar
3. dei gjenståande underbileta.
Du kan bruke `order=inside_out` for å snu bileteval (nyttig viss `batch_size>1` og du vil etikettér batchane).

**Justering**
* Viss ei etikett blir brytt til neste linje vert heile aksen sett på som "multiline" og justerast øvst med justert mellomrom.
* Viss alle etikettane er tal eller alle endar på tal (t.d. `strength: 1.`) vert heile aksen sett på som "numeric" og justerast til høgre.
* All annan tekst vert sett på som "singleline" og justerast sentrert.
* Justerer singleline og numeriske etikettar for kolonnar nedst, og for rader vert dei justert loddrett i midten.

**Skriftstorleik**
* Høgda på kolonneetikettområdet vert bestemt av `font_size` eller `halvparten av største underbilethøgd i ein rad` (kva som er større).
* Breidda på radetikettområdet vert bestemt av breidda på dei breiste underbileta (med ein minimum på 256px).
* Teksten blir krympa til den passar (ned til `font_size_min=6`) og brukar same skriftstorleik for heile aksen (radetikettar eller kolonneetikettar).
Viss skriftstorleiken allereie er på minimum, blir eventuelt overskytande tekst klippt.

**Underbiletpakking**
Formar underbileta (vanlegvis frå batchar) til det mest kvadratiske området («underbiletpakkinga»), med mindre `output_is_list=True`, i så fall vert berre eitt bilete brukt per celle og ein oppretter ei liste med heile bilete-rutenett.
Du kan bruke denne lista over bilete-rutenett for å kopla til ein annan XyzGridPlot-node for å lage super-rutenett.
Viss underbileta består av batchar med ulik storleik, fyller ein opp manglande celler med tomme bilete.
Talet på bilete per celle (inkludert batcha bilete) må vere ein multiplum av `rows * columns`.

### Inndata

| Namn | Type | Skildring |
| --- | --- | --- |
| `images` | `IMAGE` | ei liste over bilete (inkludert batchar) |
| `row_labels` | `*` | radetiketttekstar til venstre |
| `col_labels` | `*` | kolonneetiketttekstar øvst |
| `gap` | `INT` | mellomrom mellom underbiletpakkingane. Merk at inni underbileta sjølv brukar det ingen mellomrom. Viss du vil ha mellomrom mellom underbileta, kopla til ein annan XyzGridPlot-node. |
| `font_size` | `FLOAT` | målskriftstorleik. Teksten vil bli krympa til den passar (ned til `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | tekstorientering av radetikettane. Nyttig viss du vil spare plass. |
| `order` | `BOOLEAN` | definerer i kva rekkjefølgje bileta skal bli handsama. Dette er berre relevant viss du har underbilete. Nyttig viss `batch_size>1` og du vil plotte batchane. |
| `output_is_list` | `BOOLEAN` | Dette er berre relevant viss du har underbilete eller vil lage super-rutenett. |

### Utdata

| Namn | Type | Skildring |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | XYZ-GridPlot-biletet. Viss `output_is_list=True` oppretter ein liste over bilete som du kan kopla til ein annan XYZ-GridPlot-node for å lage super-rutenett. |

