$(document).ready(function () {
  var selectedIds = [];

  $("#tasks").on("check.bs.table uncheck.bs.table", function (e, row) {
    var id = row.ID;
    if (e.type === "check") {
      if (!selectedIds.includes(id)) {
        selectedIds.push(id);
      }
    } else {
      selectedIds = selectedIds.filter(function (value) {
        return value !== id;
      });
    }
    document.getElementById("selectedTasks").textContent = selectedIds.join(",");
  });

  // Handle check-all and uncheck-all separately
  $("#tasks").on("check-all.bs.table", function (e) {
    // Assuming getSelections is a method to get all selected rows. This might vary based on the actual table library you're using.
    var allRows = $("#tasks").bootstrapTable("getSelections");
    selectedIds = allRows.map(function (row) {
      return row.ID;
    });
    document.getElementById("selectedTasks").textContent = selectedIds.join(",");
  });

  $("#tasks").on("uncheck-all.bs.table", function (e) {
    selectedIds = [];
    document.getElementById("selectedTasks").textContent = "";
  });
});

$(document).ready(function () {
  var selectedIds = [];

  $("#models").on("check.bs.table uncheck.bs.table", function (e, row) {
    var id = row.ID;
    if (e.type === "check") {
      if (!selectedIds.includes(id)) {
        selectedIds.push(id);
      }
    } else {
      selectedIds = selectedIds.filter(function (value) {
        return value !== id;
      });
    }
    document.getElementById("selectedModels").textContent = selectedIds.join(",");
  });

  // Handle check-all and uncheck-all separately
  $("#models").on("check-all.bs.table", function (e) {
    // Assuming getSelections is a method to get all selected rows. This might vary based on the actual table library you're using.
    var allRows = $("#models").bootstrapTable("getSelections");
    selectedIds = allRows.map(function (row) {
      return row.ID;
    });
    document.getElementById("selectedModels").textContent = selectedIds.join(",");
  });

  $("#models").on("uncheck-all.bs.table", function (e) {
    selectedIds = [];
    document.getElementById("selectedModels").textContent = "";
  });

  $('input[aria-label="model_args"]').on("input", function () {
    var modelArgs = $(this).val();
    document.getElementById("modelArgs").textContent = modelArgs;
  });
});
