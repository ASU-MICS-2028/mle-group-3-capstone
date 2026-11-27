# Problem framing — AirWatch Accra

Owner: Eric (Problem lead) · Reviewer: Kobina · Status: **draft skeleton**

> How to use this file: facts that come from sources are filled in and cited. Every
> `[YOUR WORDS: …]` is a judgement or explanation that must be written by Eric, in his own
> voice, because this text feeds the report and the oral defence. Delete each prompt once
> it is answered.

## 1. The decision in one sentence

[YOUR WORDS: one sentence naming the decision-maker, the decision, and when it is made.
Template to adapt: "Each evening, a ___ decides whether ___ tomorrow, using ___."]

## 2. The decision-maker

| Question | Answer |
|---|---|
| Who decides? | [YOUR WORDS: e.g. a school head, a district environmental health officer, or both? Pick one primary user.] |
| When do they decide? | [YOUR WORDS: what time in the evening, and why then?] |
| What action can they take? | [YOUR WORDS: e.g. move PE and assemblies indoors; alert parents of children with asthma.] |
| What do they do today, without our tool? | [YOUR WORDS: what information, if any, do they use now?] |
| What happens if they do nothing? | [YOUR WORDS] |

## 3. Why it matters here

- Air pollution caused about 1.1 million deaths across Africa in 2019 (697,000 household,
  394,000 ambient) [1].
- In 2019, illness and death from air pollution cost Ghana an estimated $1.63 billion,
  0.95% of GDP [1].
- In Accra, mean PM2.5 was 89 µg/m³ in the Harmattan season (November–February) against
  23 µg/m³ in the rest of the year, and annual levels remain two to four times the WHO
  guideline [2].
- The WHO guideline for the 24-hour mean is 15 µg/m³ [3].

[YOUR WORDS: two or three sentences on why a next-day warning helps *this* user, and who
benefits most (children, people with asthma).]

## 4. The ML task

| Item | Definition |
|---|---|
| Type | Supervised binary classification |
| Unit of prediction | One sensor site on one day (a "site-day") |
| Label | 1 if the site's 24-hour mean PM2.5 on day D+1 is above `PM25_THRESHOLD` (35 µg/m³, in `src/config.py`); otherwise 0 |
| Prediction made | Evening of day D |
| Information allowed | Only data available by the cut-off on day D: PM2.5 history and weather up to then |
| Main metric | Recall on the positive class, with precision kept above an agreed floor (section 6) |

[YOUR WORDS: in two sentences, why this is classification and not regression, and why it is
supervised.]

### Open choice: the exact threshold

The US EPA's 2024 index puts 35.5 µg/m³ and above in "Unhealthy for Sensitive Groups"; the
"Moderate" band ends at 35.4 [4]. Our proposal says "above 35", so a day at 35.2 counts as
unhealthy for us but "Moderate" on the EPA scale. The WHO daily guideline (15 µg/m³) is much
stricter [3].

[YOUR WORDS: keep 35, switch to 35.4 to match the EPA band exactly, or argue for something
else? Note: a lower threshold makes more days positive and changes the class balance.]

### Open choice: the daily cut-off time

[YOUR WORDS: what time on day D does the app make its prediction (e.g. 6 pm, 9 pm)? Readings
after that time cannot be used. Tell Clifford and Mubarak, because it changes how the daily
average and the features are built.]

## 5. What a wrong answer costs

| Model says | What really happens | Name | Consequence for the user |
|---|---|---|---|
| "Warning" | Air was unhealthy | True positive | [YOUR WORDS] |
| "Likely safe" | Air was unhealthy | **False negative (missed bad day)** | [YOUR WORDS: who is harmed, and how?] |
| "Warning" | Air was fine | False positive (false alarm) | [YOUR WORDS: what is lost? What happens to trust if this happens often?] |
| "Likely safe" | Air was fine | True negative | [YOUR WORDS] |

[YOUR WORDS: which error is worse, and roughly how much worse? For example, "we would accept
about N false alarms to avoid one missed bad day, because …".]

## 6. Target to agree with the Modelling lead

To be agreed with Mubarak before model selection (Week 12–13):

- Minimum recall: [YOUR WORDS + Mubarak]
- Lowest acceptable precision: [YOUR WORDS + Mubarak]
- How the warning threshold on the model's probability will be chosen: on the validation
  folds only, never on the test set.

## 7. Scope

In scope:
- Sensor sites in Greater Accra with enough data (the Data lead's completeness check decides).
- Next-day prediction only.

Out of scope:
- Forecasting more than one day ahead.
- Neighbourhoods with no sensor (to be listed by the Ethics lead as a limitation).
- Replacing official Ghana EPA alerts: the tool is advice only.
- Stretch goal only: testing the Accra model on Lagos.

## 8. User conversation (task P3)

[Fill in after talking to a teacher or school head, if possible: date, role (no names
needed), what they said about timing, wording and whether they would use it.]

## Sources

1. S. Fisher *et al.*, "Air pollution and development in Africa: impacts on health, the economy,
   and human capital," *Lancet Planetary Health*, vol. 5, no. 10, pp. e681–e688, 2021.
2. A. S. Alli *et al.*, "Spatial-temporal patterns of ambient fine particulate matter (PM2.5) and
   black carbon (BC) pollution in Accra," *Environmental Research Letters*, vol. 16, no. 7,
   074013, 2021.
3. World Health Organization, *WHO global air quality guidelines*, 2021 (PM2.5: 15 µg/m³ 24-hour,
   5 µg/m³ annual).
4. US EPA, "Final updates to the Air Quality Index for particle pollution: fact sheet," Feb. 2024.
   https://www.epa.gov/system/files/documents/2024-02/pm-naaqs-air-quality-index-fact-sheet.pdf

## AI-use declaration

[YOUR WORDS: state that Claude drafted this skeleton, filled in the cited facts and the ML task
definition, and that the judgements in sections 1, 2, 4, 5 and 6 are your own.]
