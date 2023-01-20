**REPORT - PRECOG RECRUITMENT TASK**

\- By Ashna Dua

**DATA AND TASK DESCRIPTION:**

The Development Data Lab (DDL) is an esteemed organization that employs the utilization of data analysis and visualization to illuminate policy and decision-making in developing nations. They are acclaimed for producing a plethora of data sets, consisting of information pertaining to the judiciaries of several countries, including but not limited to court case backlogs, judicial budgets, and the number of judges and court staff. The purpose of this data is to assist policymakers, researchers, and other stakeholders to comprehend and tackle issues related to the efficiency and functioning of judiciaries in developing countries. This data can be utilized to detect patterns and trends, pinpoint areas in need of amelioration, and monitor progress over time.

The Judicial Data produced by the Development Data Lab was provided for the purpose of exploration and analysis in the PreCog Recruitment Task. This task is divided into two parts, Analysis and Classification, which require the necessary preprocessing and plotting steps to be carried out.

**PART 1: ANALYSIS **
**CASE LOAD:**

In the legal field, a case load refers to the number of cases or clients that a lawyer, judge or legal organization is responsible for handling at a given time. A case load for a judge refers to the number of cases that a judge is responsible for hearing and making decisions on at a given time. This can include criminal cases, civil lawsuits, and other legal matters that come before the court. A judge's case load can vary depending on the type of court they preside over, the area in which they serve, and the overall workload of the court system.

A judge who has a heavy caseload may have a plethora of cases scheduled for trial or hearing at any one time, and may be required to proceed expeditiously to keep pace with the volume, whereas a judge with a lighter case load may have fewer cases to hear and may be able to devote more time to each case.

Also, in some jurisdictions, judges are assigned to specific types of cases, such as criminal, civil, or family law, and their caseload will reflect the type of cases they are assigned to hear. Upon conducting a thorough analysis of the data, the mean caseload per judge of each state was meticulously plotted, and the variation in this case load over the years was observed.

This examination revealed that judges in the states of Chandigarh, Delhi, and Punjab were faced with the most substantial case loads, whereas judges in the states of Sikkim, Meghalaya, Mizoram, and Tripura were comparatively less burdened.

![](https://github.com/ashnadua01/Precog/blob/main/Analysis/GIFS-representingTrend/caseLoad.gif)

METHOD:

The Pandas Library of Python, a powerful tool for data manipulation and analysis, was utilized to scrutinize the data of the cases over the years, as well as the data of the judges. The calculation of the caseload was executed in the following manner:

![](https://github.com/ashnadua01/Precog/blob/main/Reference/India%20Shape/equation.png)

The caseload for each state was calculated and plotted with precision, and the trend was studied with great attention from 2010 to 2018.


**GENDER BIAS:**

Gender bias refers to the preferential treatment or prejudice towards individuals based on their gender. This can manifest in a variety of forms, including discrimination, stereotypes, and societal expectations. Gender bias can be both conscious and unconscious, and it can affect both men and women, although it is more commonly directed towards women. It can occur in various settings such as the workplace, education, and healthcare, including the judicial system.

Gender bias can have negative consequences on individuals, organizations, and society as a whole, by limiting opportunities, hindering performance and productivity, and promoting inequality.

An examination of the number of criminal and civil cases presided over by judges revealed that the proportion of cases handled by women is significantly less than 50\%, indicating a pervasive and persistent gender bias within the legal system. While the percentage of women handling criminal and civil cases has been gradually increasing over the years, it will take a considerable amount of time at this rate to achieve a state of parity.

![](https://github.com/ashnadua01/Precog/blob/main/Analysis/GIFS-representingTrend/genderBias.gif)

METHOD:

In order to demonstrate the presence of gender bias among judges handling criminal and civil cases, the Pandas and Plotly libraries of Python were employed. The datasets of acts and sections were seamlessly integrated with the cases dataset and the judge dataset to facilitate the identification of the genders of the judges handling said cases.

Utilizing the Plotly library, these results were graphically represented through the use of pie charts, depicting the proportion of men and women handling these cases respectively, thus offering a clear and concise visual representation of the gender bias present in the legal system.

**PENDING CASES:**

Pending cases, within the Indian judicial system, are those legal proceedings that have been initiated and are yet to be resolved or decided upon by a judge or a bench of judges. These cases comprise of a wide spectrum of legal disputes, ranging from criminal trials, civil lawsuits, appeals, and more.

The phenomenon of pending cases has been a chronic problem plaguing the Indian judiciary for quite some time now. This can be attributed to various reasons, such as an inadequate number of judges, insufficient resources, and an overwhelming backlog of cases. These factors have resulted in an overburdened legal system, leading to delays and inefficiencies in the administration of justice.

Upon conducting a thorough analysis of the decision dates of cases, a map was carefully plotted to give a comprehensive overview of the number of cases pending in each state.The findings of this analysis reveal that over the years, the maximum number of pending cases are observed in the state of Uttar Pradesh, indicating a significant backlog of unresolved legal matters in this region.

On the other hand, the least number of pending cases are observed in the states of East India, indicating a more efficient and streamlined legal system in these areas. This map serves as a valuable tool for identifying areas in need of improvement and for implementing targeted measures to address the issue of pending cases.

![](https://github.com/ashnadua01/Precog/blob/main/Analysis/GIFS-representingTrend/pendingCases.gif)

METHOD:

In order to provide a visual representation of the number of pending cases in each state, the Pandas and GeoPandas libraries of Python were employed. The number of pending cases were determined through a calculation that took into account the number of cases in a given year, whose decision date had not yet been reached by December 31st of that year.

Utilizing the GeoPandas library, these results were plotted on a map of India, with each state being represented by a color corresponding to a scale that indicated the number of pending cases. This graphical representation offered a clear and concise understanding of the distribution of pending cases across the states of India.


**DISPOSITIONS:**

In the realm of judicial proceedings, disposition refers to the ultimate resolution or pronouncement of a case, signifying the final act of determining the outcome of the legal matter at hand. It pertains to the final judgment or ruling issued by a court or other judicial body vested with the authority to decide legal matters. The disposition of a case can encompass a wide range of possible outcomes, such as a verdict of guilt or innocence in a criminal trial, an award of compensation in a civil lawsuit, or an order for a specific action to be taken in a legal dispute.

These dispositions are the culmination of the judicial process and serve as the official resolution of the case, bringing closure to all parties involved. The disposition of a case is typically recorded in a written document, known as a judgment or opinion, which provides a detailed explanation of the rationale and legal reasoning behind the decision, serving as a legal precedent for future cases.

Upon conducting a meticulous and exhaustive examination of the corpus of legal cases, it was observed that there existed a discernible pattern in the frequency of various types of dispositions awarded. The most prevalent dispositions that were meted out were those that were disposed-otherwise, allowed, and acquitted.

These dispositions were found to be the most commonly occurring outcomes in the dataset of cases analyzed. Furthermore, this trend was not limited to a specific jurisdiction or area of law, but rather was a pervasive phenomenon across the entire dataset. This observation can be of great utility in the prediction of future dispositions and the formulation of legal strategies, as well as providing valuable insight into the functioning of the judicial system.

METHOD:

In order to chart the aggregate number of dispositions in each year, the Plotly library was employed to create a bar graph, wherein each bar represented a distinct disposition. This graph offered a valuable perspective into the ultimate determination of the majority of cases, by providing a visual representation of the frequency of each disposition over time. This approach was particularly useful in identifying any temporal variations in the distribution of dispositions, thereby allowing for a more informed understanding of the judicial process.
