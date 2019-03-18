 -*- coding: utf-8 -*-

import sys
import pandas as pd
from googleads import adwords


def main(client):
  # Initialize appropriate service.
  report_downloader = client.GetReportDownloader(version='v201809')

  # Create report query.
  report_query = (adwords.ReportQueryBuilder()
                  .Select('CampaignName', 'AdGroupId', 'Id', 'Criteria',
                          'CriteriaType', 'FinalUrls', 'Impressions', 'Clicks',
                          'Cost')
                  .From('CRITERIA_PERFORMANCE_REPORT')
                  .Where('Status').In('ENABLED', 'PAUSED')
                  .During('LAST_7_DAYS')
                  .Build())

  # You can provide a file object to write the output to. For this
  # demonstration we use sys.stdout to write the report to the screen.
  # writer = pd.ExcelWriter('Datanew.xlsx')
  with open('auction_data_from_google_report.csv', 'w', encoding='utf-8') as fp:
	  report_downloader.DownloadReportWithAwql(
		  report_query, 'CSV', fp, skip_report_header=False,
		  skip_column_header=False, skip_report_summary=False,
		  include_zero_impressions=True)



if __name__ == '__main__':
  # Initialize client object.
  adwords_client = adwords.AdWordsClient.LoadFromStorage()

  main(adwords_client)


