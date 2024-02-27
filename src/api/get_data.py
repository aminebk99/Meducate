 
import requests
from prompts.get_data import GetDataPrompt
from core import BafLog
from llms.openai_llm import OpenAILLM

logger = BafLog

class GetDataAPI:
   def __init__(self):
    print("init tool")

   def process(self):
    #article = "RWANDA FDA KICK-STARTS €2M TWINNING PROJECT TO IMPROVE 'ANSM will be removed ' MEDICINAL PRODUCTS May 25, 2023/0 Comments/in News/by FDA IT Rwanda Foods and Drugs Authority has welcomed the EU-funded project dubbed “Twinning project” to strengthen the Authority in regulating medicinal products including vaccines.\n\nThe project launched on May 16, 2023 aims to promote drugs and food safety in Rwanda.\n\nThe launch brought together key stakeholders in the health sector, including government officials, health industry representatives, civil society organizations, and development partners.\n\nThe project was funded by the European Union Delegation and is implemented by Expertise France, a French technical cooperation Agency with the help of different health agencies of the European partner countries of the twinning.\n\nThe two-year project, to be implemented at the cost of 2 million Euros, seeks to improve its laboratory services, enhancing its capacity for risk assessment, and promoting the use of international standards and best practices.\n\nThe twinning project involves several vaccines and medicines regulatory agencies from EU Member States such as the French National Agency for the Safety of Medicines and Health Products (ANSM), Paul-Ehrlich-Institut – German Federal Institute for Vaccines and Biomedicines, Sciensano of Belgium and the State Medicines Control Agency of Lithuania.\n\nSpeaking during the launch, Dr. Yvan Butera, State Minister in the Ministry of Health commended team Europe for the continuous support and effort rendered to the health sector in Rwanda.\n\n“A main priority for the Government of Rwanda is to strengthen health systems at all levels of service delivery in order to ensure universal accessibility of equitable and affordable quality health services for all Rwandans,” he said.\n\nOne of the country’s strategies to address this objective, he said, is to enhance the domestic value chain for pharmaceutical and vaccine manufacturing, which requires strengthening the national regulatory framework.\n\n“This is the overall goal of this EU Twinning Project, which aims at strengthening Rwanda FDA’s regulatory functions related to medicinal products including vaccines,” he noted.\n\nThe project also looks at Strengthening of market surveillance and control function – vigilance and laboratory testing functions as well as supporting the establishment of the official batch release function for vaccines.\n\n“The launch of this twinning project, which follows the agreement that was signed in June 2022, is a major step toward realizing the country’s goals of ensuring equitable and affordable access to quality health services for all Rwandans through quality regulation of medical products,” Minister of state said.\n\nSince its implementation in October 2022, this twinning program has enabled the regulatory body-Rwanda FDA to adapt best practices borrowed from sister European regulatory agencies to Rwanda context, he said.\n\n“We have no doubt that Rwanda FDA will keep up-to-date with the current innovations and developments in technology within the regulatory environment globally,” he added.\n\nHe appreciated the efforts deployed through the European Commission by the consortium partner countries to support the Republic of Rwanda in strengthening its medicines’ regulatory framework.\n\nIt is expected that about 200 experts will be able to support the Rwanda FDA through field visits during which they will share their expertise with designated Rwanda FDA Staff.\n\nThe project team consists of experts from health agencies from the European member states which are part of the twinning who will work together with Rwanda FDA Staff to achieve the project objectives.\n\nIt is set to provide the Rwanda FDA with access to support from EU National Regulatory Agencies.\n\nEU Ambassador to Rwanda, Belén Calvo Uyarra said: “EU is a proud partner of Rwanda in manufacturing and access to vaccines, medicines and health equity.”\n\n“In Sub-Saharan Africa, no other Twinning cooperation has attracted such a sizable consortia. As every Member State involved can bring their own areas of expertise, we are confident that this partnership will bring you the highest possible value,” she noted.\n\nWith Rwanda soon to start producing vaccines, this twinning cooperation provides support with a view to ensure Rwanda FDA has the necessary regulatory procedures in place for future vaccine manufacturing, she added."
    #article = "In the Medication/Pharmaceutical category, two significant drugs, Levothyroxine and Ferrous Sulfate, stand out under the Denomination Commune Internationale (DCI) classification. Levothyroxine, classified as such, is a synthetic thyroid hormone crucial for treating hypothyroidism. By restoring optimal thyroid hormone levels, it alleviates symptoms and enhances the well-being of individuals with an underactive thyroid."
    article = """

  The pharmaceutical landscape is set to undergo a significant shift with the recent announcement concerning the diabetes medication Acarbose. In a surprising development, authorities in the United States have decided to block the distribution and sale of Acarbose effective November 25, 2023. This decision follows extensive testing and research conducted by PRE-LABO, a renowned Canadian laboratory specializing in pharmaceutical analysis.

PRE-LABO's findings, which have been published and scrutinized by the medical community, suggest potential risks associated with Acarbose that had not been previously identified. While the specific details of these risks have not been fully disclosed to the public, the laboratory's reputation for thorough and unbiased testing lends significant weight to their recommendations. Consequently, the U.S. health authorities have taken the precautionary measure of halting Acarbose's availability, prioritizing patient safety amidst these new concerns.
In another major development, Acetyleucine, a medication widely used for treating vertigo and balance disorders, is set to undergo a significant transformation. The pharmaceutical industry has announced that Acetyleucine will be rebranded and reformulated as "Acetyleucine V2" starting next year. This change will be implemented worldwide, reflecting a global shift in the medication's composition and possibly its therapeutic approach.

While details about the differences between the original Acetyleucine and the upcoming "Acetyleucine V2" are still under wraps, experts speculate that the new formulation may offer enhanced efficacy, reduced side effects, or improved patient compliance. This development highlights the pharmaceutical industry's ongoing commitment to innovation and improvement, constantly seeking to enhance the safety and effectiveness of medications for patients across the globe.

Conclusion

These changes in the statuses of Acarbose and Acetyleucine mark significant events in the pharmaceutical field, reflecting an industry that is always evolving and adapting. As the medical community and patients alike await further details, these developments underscore the importance of continuous research and vigilance in drug safety and efficacy.

"""

    categories = ["Telemedicine Education", "Global Health Education", "Patient-Centered Care", "Medical Ethics Education", "Continuing Medical Education (CME)", "Interprofessional Education (IPE)"]
    dci = ["Rwanda FDA", "ANSM", "SwissMedic"]

    dciAndCategories = f""" 
        dci = {dci}
        categories = {categories}
    """

    result_prompt = GetDataPrompt.get_data_prompt(data=dciAndCategories)
    # print("test prompt ", result_prompt)

    result = OpenAILLM.process(self, message=article, prompt=result_prompt)
    print("***************************************************")
    print(result)
    print("***************************************************")
    return result
        