// Bu faylni GitHub'ga emas, Google Apps Script muharririga joylashtirasiz.
// Yo'riqnoma README.md dagi "Google Sheets ulash" bo'limida.

function doPost(e) {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const order = JSON.parse(e.postData.contents);

  const itemsText = (order.items || [])
    .map((i) => `${i.product} x${i.quantity} (${i.color || "-"}, ${i.size || "-"})`)
    .join("; ");

  sheet.appendRow([
    new Date(order.timestamp || Date.now()),
    order.business || "",
    itemsText,
    order.deliveryOrPickup || "",
    order.customerPhone || "",
    order.customerName || "",
    order.estimatedTotal || "",
  ]);

  return ContentService.createTextOutput(
    JSON.stringify({ status: "ok" })
  ).setMimeType(ContentService.MimeType.JSON);
}
