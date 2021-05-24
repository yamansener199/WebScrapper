function AutoSortOnEdit() {
  var sheetName = "Sayfa1";
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(sheetName);
  var range = sheet.getRange(2, 1, sheet.getLastRow()-1 , sheet.getLastColumn());
  range.sort({column: 4, ascending: true});
}
function onOpen() { 
  // Try New Google Sheets method
  try{
    var ui = SpreadsheetApp.getUi();
    ui.createMenu('SendMail')
    .addItem('Send Report', 'getGoogleSpreadsheetAsExcel')
    .addToUi(); 
  }
  // Log the error
  catch (e){Logger.log(e)}
}
function getGoogleSpreadsheetAsExcel(){
  try {
    var ss = SpreadsheetApp.getActive();
    var const_url="https://docs.google.com/feeds/download/spreadsheets/Export?key=";
    var const_boss_email="okan@analyticahouse.com";
    var url = const_url+ ss.getId()+"&exportFormat=xlsx";
    var params = {
      method      : "get",
      headers     : {"Authorization": "Bearer " + ScriptApp.getOAuthToken()},
      muteHttpExceptions: true
    };
    var blob = UrlFetchApp.fetch(url, params).getBlob();
    blob.setName(ss.getName() + ".xlsx");
    MailApp.sendEmail(const_boss_email, "CaseStudy Done ", "It was a pleasure for me to do this assigment.On the other hand I tried to sort data but 100.0 value can't fit to compare ,    have no idea why :( I also tried to do the bonus but parsing the components was a little bit hard :/ Thank you !", {attachments: [blob]});
  } catch (f) {
    Logger.log(f.toString());
  }
}
onOpen();
getGoogleSpreadsheetAsExcel();

