from crewai import Task

class FinanceTasks:
    def __init__(self, tools):
        self.tools = tools

    def current_stock_analysis(self, agent):
        return Task(
            description='Conduct an in-depth analysis of the current performance of {company}',
            expected_output=("Summary of {company}'s recent financial performance, including key financial metrics such as revenue, earnings, and profit margin."
                              "Evaluation of {company}'s market position and competitive landscape, highlighting key strengths and weaknesses."
                              "Analysis of recent news and events impacting {company}'s stock price, with insights into investor sentiment and market reaction."
                              "Assessment of any recent regulatory developments or legal proceedings affecting {company}'s operations."),
            agent=agent,
            async_execution=True,
            tools=self.tools
        )

    def current_market_analysis(self, agent):
        return Task(
            description='Analyze current market trends and dynamics',
            expected_output=("Overview of current market conditions, including major indices (e.g., S&P 500, NASDAQ) and sector performance."
                              "Assessment of macroeconomic factors influencing market sentiment, such as interest rates, inflation, and economic growth."
                              "Analysis of recent market volatility and trading activity, with insights into investor behavior and sentiment."
                              "Evaluation of geopolitical events and their potential impact on global markets."),
            agent=agent,
            async_execution=True,
            tools=self.tools
        )

    def news_and_social_media_analysis(self, agent):
        return Task(
            description='Analyze news articles and social media sentiment related to {company}',
            expected_output=("Summary of recent news articles and social media discussions related to {company}, highlighting key themes and sentiment."
                              "Identification of any significant news events or trends impacting {company}'s stock price and market sentiment."
                              "Analysis of sentiment trends on social media platforms (e.g., Twitter, Reddit) regarding {company}, including sentiment polarity and volume."
                              "Insights into how news and social media sentiment may influence investor behavior and market dynamics."),
            agent=agent,
            async_execution=True,
            tools=self.tools
        )

    def quantitative_and_technical_analysis(self, agent):
        return Task(
            description='Perform quantitative and technical analysis for {company} stock',
            expected_output=("Quantitative analysis of {company}'s historical stock price data, including statistical measures such as mean, median, standard deviation, and correlation."
                              "Technical analysis of {company}'s stock price chart, identifying key support and resistance levels, trend patterns, and trading signals."
                              "Evaluation of common technical indicators (e.g., moving averages, RSI, MACD) to assess {company}'s stock price momentum and trend strength."
                              "Identification of potential entry and exit points for trades based on quantitative and technical analysis. "
                              "Also predict next 5 dates and their corresponding stock price."),
            agent=agent,
            async_execution=True,
            tools=self.tools
        )



    def risk_assessments(self, agent):
        return Task(
            description='Conduct risk assessments for investing in {company} stock',
            expected_output=("Identification and evaluation of key investment risks associated with {company}, including market risk, liquidity risk, and regulatory risk."
                              "Quantitative analysis of historical volatility and downside risk metrics for {company}'s stock."
                              "Stress testing scenarios to assess the potential impact of adverse market conditions on {company}'s stock price."
                              "Recommendations for risk management strategies and portfolio diversification techniques to mitigate investment risks."),
            agent=agent,
            async_execution=False,
            tools=self.tools
        )

    def investment_advice(self, agent):
        return Task(
            description='Provide investment advice and recommendations for {company} stock',
            expected_output=("Personalized investment recommendations tailored to individual risk tolerance, investment goals, and time horizon."
                              "Portfolio allocation suggestions based on the analysis of {company} stock and broader market trends."
                              "Long-term investment thesis for {company}, including potential growth drivers, competitive advantages, and valuation considerations."
                              "Short-term trading strategies and tactics based on quantitative and technical analysis indicators. "
                              "Also predict next 5 dates and their corresponding stock price."),
            agent=agent,
            async_execution=False,
            tools=self.tools
        )
    
    def extract_stock_predictions(self, agent):
        return Task(
            description='Extract the next 5 upcoming dates and corresponding stock prices from the given stock prediction report',
            expected_output=("A list format containing the next 5 upcoming dates and their corresponding stock prices."
                            "Dates should be extracted accurately from the prediction report and formatted as dates = [date1, date2, date3, date4, date5]."
                            "Corresponding stock prices should be formatted as values = [value1, value2, value3, value4, value5]."),
            agent=agent,
            async_execution=False,
            tools=self.tools
        )
    

    def generate_report(self, agent):
        return Task(
            description=("Provide comprehensive analysis and investment recommendations for {company} stock, "
                        "including current stock performance, market trends, news and social media analysis, "
                        "quantitative and technical analysis, risk assessments, and investment advice."),
            expected_output = """
                    **Current Analysis**  
                    Detailed analysis of {company} stock performance, including trends and factors affecting its valuation.

                    **In-Depth Examination**  
                    In-depth examination of broader market trends and their implications for {company} stock.

                    **News and Social Media**  
                    Analysis of news and social media sentiment surrounding {company} and its impact on stock performance.

                    **Quantitative and Technical Analysis**  
                    Quantitative and technical analysis of {company} stock, identifying key indicators and patterns.

                    **Risk Assessments**  
                    Risk assessments, highlighting potential risks and their mitigation strategies.

                    **Investment Strategy**  
                    [Buy/sell] at [value] and [sell/buy] at [value]
                    """,
            agent=agent,
            async_execution=False,
            tools=self.tools
)
