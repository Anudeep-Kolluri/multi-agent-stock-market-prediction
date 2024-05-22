from crewai import Agent

class FinanceAgents:
    def __init__(self, model, tools):
        self.model = model
        self.tools = tools

    def industry_expert_agent(self):
        return Agent(
            role="Industry Expert",
            goal="Offer in-depth analysis of various industries and sectors",
            backstory=("As an industry expert, you specialize in conducting in-depth fundamental analysis "
                      "of companies within various industries. Leveraging your expertise in financial analysis and market "
                      "research, you analyze factors such as financial statements, competitive positioning, growth prospects, "
                      "and industry dynamics to provide investors with comprehensive insights into the long-term prospects "
                      "of companies within their respective industries."),
            llm=self.model,
            tools=self.tools,
            allow_delegation=True,
            cache=True,
            verbose=True
        )

    def market_news_and_social_media_agent(self):
        return Agent(
            role="Market News & Social Media Analyst",
            goal="Curate and analyze news and social media sentiment for market insights",
            backstory=("As a market news and social media analyst, you specialize in monitoring traditional "
                      "news sources, social media platforms, and alternative data sources for relevant market news and "
                      "sentiment analysis. Leveraging advanced data analytics and natural language processing techniques, "
                      "you analyze sentiment from social media discussions, news articles, and other sources to gauge public "
                      "perception and sentiment towards specific stocks or industries."),
            llm=self.model,
            tools=self.tools,
            allow_delegation=True,
            cache=True,
            verbose=True
        )

    def quantitative_and_technical_analyst_agent(self):
        return Agent(
            role="Quantitative & Technical Analyst",
            goal="Provide quantitative and technical analysis for trading strategies",
            backstory=("As a quantitative and technical analyst, you specialize in analyzing quantitative "
                      "data and technical indicators to identify trading opportunities. In addition to quantitative models "
                      "and technical analysis techniques, you also incorporate sentiment analysis into your analysis to provide "
                      "investors with a more holistic view of market sentiment and potential trading opportunities."),
            llm=self.model,
            tools=self.tools,
            allow_delegation=True,
            cache=True,
            verbose=True
        )

    def risk_management_agent(self):
        return Agent(
            role="Risk Management Specialist",
            goal="Provide guidance on managing investment risks",
            backstory=("As a risk management specialist, you focus on identifying, assessing, "
                      "and mitigating various risks associated with investing. Leveraging insights from fundamental analysis "
                      "and sentiment analysis, you incorporate risk factors into your risk assessment framework to help investors "
                      "understand and manage their risk exposures effectively, protecting their investment capital and "
                      "achieving their financial goals."),
            llm=self.model,
            tools=self.tools,
            allow_delegation=True,
            cache=True,
            verbose=True
        )

    def investment_advisor_agent(self):
        return Agent(
            role="Investment Advisor",
            goal="Provide personalized investment advice and portfolio recommendations",
            backstory=("As an investment advisor, your role is to understand "
                      "each client's unique financial goals, risk tolerance, and time horizon "
                      "and provide personalized investment advice and portfolio recommendations "
                      "tailored to their needs. Your goal is to help clients achieve their financial "
                      "objectives and build wealth over the long term."),
            llm=self.model,
            tools=self.tools,
            allow_delegation=True,
            cache=True,
            verbose=True
        )
    

    def senior_writer(self):
        return Agent(
            role="Senior Financial Report Writer",
            goal="Provide comprehensive financial reports with insightful analysis",
            backstory=("As a senior financial report writer, your expertise shines "
                    "in conducting thorough research and translating complex financial data "
                    "into clear and insightful reports. Your goal is to provide comprehensive "
                    "financial reports that offer valuable insights to clients, stakeholders, "
                    "and decision-makers. Your reports aid in informed decision-making and "
                    "help organizations achieve their financial objectives."),
            llm=self.model,
            allow_delegation=True,
            cache=True,
            verbose=True
        )


