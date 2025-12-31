## Workflow Discriminator

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(Συμπεριλαμβανόμενη η ComfyUI workflow)

Συγκρίνει workflows και τα διακρίνει για να εξαγάγει τις διαφορετικές τιμές ως ξεχωριστές OutputList.
Μπορείτε να χρησιμοποιήσετε αυτόν τον κόμβο για να επαναφέρετε τον τρόπο που δημιουργήθηκε κάθε μεμονωμένη εικόνα από μια λίστα εικόνων με το ίδιο workflow.
Σημειώστε ότι το `IMAGE` του ComfyUI δεν περιέχει τα μεταδεδομένα workflow και πρέπει να φορτώσετε τις εικόνες με ειδικούς φορτωτές εικόνων+μεταδεδομένων και να συνδέσετε τα μεταδεδομένα σε αυτόν τον κόμβο.
Οι προσαρμοσμένοι κόμβοι με φορτωτές μεταδεδομένων περιλαμβάνουν:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Εισόδοι

| Όνομα | Τύπος | Περιγραφή |
| --- | --- | --- |
| `objs_0` | `*` | (προαιρετικό) Ένα μεμονωμένο αντικείμενο (ή μια λίστα αντικειμένων), συνήθως από ένα workflow. Τα `objs_0` και `more_objs` θα συνδεθούν μαζί και υπάρχουν για ευκολία, αν θέλετε να συγκρίνετε μόνο δύο αντικείμενα. |
| `more_objs` | `*` | (προαιρετικό) Ένα άλλο αντικείμενο (ή μια λίστα αντικειμένων), συνήθως από ένα workflow. Τα `objs_0` και `more_objs` θα συνδεθούν μαζί και υπάρχουν για ευκολία, αν θέλετε να συγκρίνετε μόνο δύο αντικείμενα. |
| `ignore_jsonpaths` | `STRING` | (προαιρετικό) Μια λίστα JSONPaths για να αγνοηθούν σε περίπτωση που θέλετε να συνδέσετε πολλαπλούς διακριτικούς μαζί. |

### Έξοδοι

| Όνομα | Τύπος | Περιγραφή |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

