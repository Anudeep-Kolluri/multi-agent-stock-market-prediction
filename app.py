import streamlit as st
import os

from crewai import Crew
from crewai_tools import ScrapeWebsiteTool, SerperDevTool 

from agents import FinanceAgents
from tasks import FinanceTasks

from langchain_openai import ChatOpenAI

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
tools = [search_tool, scrape_tool]


# Set the title of the app
st.title('Multi Agent stock market analysis')

# Create session state to manage page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'form'

# Page for API key and model selection form
if st.session_state.page == 'form':
    with st.form("api_form"):
        openai_api_key = st.text_input('OPENAI API Key', type='password')
        serper_api_key = st.text_input('SERPER API Key', type='password')
        model = st.selectbox(
            'Select Model',
            ['gpt-3.5-turbo', 'gpt-4o', 'gpt-4'],
            index=0  # gpt-3.5-turbo is the default option
        )
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            st.session_state.openai_api_key = openai_api_key
            st.session_state.serper_api_key = serper_api_key
            st.session_state.model = model
            st.session_state.page = 'stock_name'

            os.environ["OPENAI_API_KEY"] = openai_api_key
            os.environ["SERPER_API_KEY"] = serper_api_key
            os.environ["OPENAI_MODEL_NAME"] = model
            
            st.rerun()

# Page for entering stock name
elif st.session_state.page == 'stock_name':
    st.write(f'Selected Model: {st.session_state.model}')
    stock_name = st.text_input('Enter Stock Name')
    if st.button('Submit'):

        llm = ChatOpenAI(
            model=st.session_state.model,
            api_key=st.session_state.openai_api_key
        )

        agents = FinanceAgents(llm, tools)
        tasks = FinanceTasks(tools)

        industry_expert_agent = agents.industry_expert_agent()
        market_news_and_social_media_agent = agents.market_news_and_social_media_agent()
        quantitative_and_technical_analyst_agent = agents.quantitative_and_technical_analyst_agent()
        risk_management_agent = agents.risk_management_agent()
        investment_advisor_agent = agents.investment_advisor_agent()
        senior_writer = agents.senior_writer()
        number_extractor = agents.number_extractor()

        current_stock_analysis = tasks.current_stock_analysis(agent=industry_expert_agent)
        current_market_analysis = tasks.current_market_analysis(agent=industry_expert_agent)
        news_and_social_media_analysis = tasks.news_and_social_media_analysis(agent=market_news_and_social_media_agent)
        quantitative_and_technical_analysis = tasks.quantitative_and_technical_analysis(agent=quantitative_and_technical_analyst_agent)
        extract_stock_predictions = tasks.extract_stock_predictions(agent = number_extractor)
        risk_assessments = tasks.risk_assessments(agent=risk_management_agent)
        investment_advice = tasks.investment_advice(agent=investment_advisor_agent)
        generate_report = tasks.generate_report(agent = senior_writer)


        investment_advice.context = [current_stock_analysis, current_market_analysis, quantitative_and_technical_analysis, risk_assessments]
        extract_stock_predictions.context = [quantitative_and_technical_analysis, investment_advice]
        generate_report.context = [current_stock_analysis, current_market_analysis, quantitative_and_technical_analysis, risk_assessments, investment_advice]

        crew = Crew(
            agents = [
                industry_expert_agent,
                market_news_and_social_media_agent,
                quantitative_and_technical_analyst_agent,
                risk_management_agent,
                investment_advisor_agent,
                senior_writer
            ],

            tasks = [
                current_stock_analysis,
                current_market_analysis,
                news_and_social_media_analysis,
                quantitative_and_technical_analysis,
                risk_assessments,
                investment_advice,
                extract_stock_predictions,
                generate_report
            ],
            verbose=True
        )

        result = crew.kickoff(inputs={"company" : stock_name})
        st.write(result)



        

