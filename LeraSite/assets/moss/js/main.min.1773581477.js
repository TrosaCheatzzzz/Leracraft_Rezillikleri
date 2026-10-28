//
// DiscordOnline ==================================
//

var DiscordOnline = (function () {
  var $onlineText = $('[data-toggle="discordonline"]');
  // Init
  function init($onlineText) {
    var $discordID = $onlineText.attr("data-discord-id");
    var $ajaxURL = 'https://discord.com/api/guilds/' + $discordID + '/widget.json';
    
    $.ajax({
      url: $ajaxURL,
      dataType: "json",
      success: function (data) {
        $onlineText.text(data["presence_count"]);
      },
    });
  }
  if ($onlineText.length) {
    $onlineText.each(function () {
      init($(this));
    });
  }
})();

//
// LazyLoad ==================================
//

var lazyLoader = new LazyLoad({
  elements_selector: ".lazyload"
});

//
// ServerOnline ==================================
//

var ServerOnline = (function() {
  var $onlineText = $('[data-toggle="onlinetext"]');
  var $onlineBox = $('[data-toggle="onlinebox"]');
  // Init
  function init($onlineText) {
    var $serverIP = $onlineText.attr("server-ip").split(':', 2);
    
    if ($onlineAPI == 1) {
      var $ajaxURL = "https://mcapi.us/server/status?ip=" + $serverIP[0] + (($serverIP[1]) ? "&port=" + $serverIP[1] : "");
    }
    else if ($onlineAPI == 2) {
      var $ajaxURL = "https://eu.mc-api.net/v3/server/ping/" + $serverIP[0] + (($serverIP[1]) ? ":" + $serverIP[1] : "");
    }
    else if ($onlineAPI == 3) {
      var $ajaxURL = "https://mcapi.tc/?" + $serverIP[0] + "/json";
    }
    else if ($onlineAPI == 4) {
      var $ajaxURL = "https://api.keyubu.net/mc/ping.php?ip=" + $serverIP[0] + ":" + (($serverIP[1]) ? $serverIP[1] : "25565");
    }
    else if ($onlineAPI == 5) {
      var $ajaxURL = "https://api.mcsrvstat.us/2/" + $serverIP[0] + (($serverIP[1]) ? ":" + $serverIP[1] : "");
    }
    else if ($onlineAPI == 6) {
      var $ajaxURL = "https://api.mcsrvstat.us/2/" + $serverIP[0] + ":" + (($serverIP[1]) ? $serverIP[1] : "19132");
    }
    else {
      var $ajaxURL = "https://mcapi.us/server/status?ip=" + $serverIP[0] + (($serverIP[1]) ? "&port=" + $serverIP[1] : "");
    }
    
    $.ajax({
      url: $ajaxURL,
      dataType: "json",
      success: function(data) {
        if ($onlineAPI == 1) {
          var onlineStatus = data["online"];
          var online = data["players"]["now"];
        }
        else if ($onlineAPI == 2) {
          var onlineStatus = data["online"];
          var online = data["players"]["online"];
        }
        else if ($onlineAPI == 3) {
          var onlineStatus = data["status"];
          var online = data["players"];
        }
        else if ($onlineAPI == 4) {
          var onlineStatus = data["online"];
          var online = data["players"]["online"];
        }
        else if ($onlineAPI == 5) {
          var onlineStatus = data["online"];
          var online = data["players"]["online"];
        }
        else if ($onlineAPI == 6) {
          var onlineStatus = data["online"];
          var online = data["players"]["online"];
        }
        else {
          var onlineStatus = data["online"];
          var online = data["players"]["now"];
        }
        
        if (onlineStatus == true || ($onlineAPI == 3 && onlineStatus != "offline")) {
          $onlineText.text(online  + ' ' + lang.players_online);
          $onlineBox.addClass("active");
        }
        else {
          $onlineText.text("0");
        }
      }
    });
  }
  if ($onlineText.length) {
    $onlineText.each(function() {
      init($(this));
    });
  }
})();

//
// CopyServerIP ==================================
//

var CopyServerIP = (function() {
  var $copyip = $('[data-toggle="copyip"]');
  // Init
  function init($copyip) {
    var clipboard = new ClipboardJS('[data-toggle="copyip"]');
    clipboard.on("success", function(e) {
      swal.fire({
        title: lang.alert_title_success,
        text: lang.alert_message_server_address_copied,
        type: "success",
        confirmButtonColor: "#02b875",
        confirmButtonText: lang.alert_btn_ok
      });
    });
  }
  if ($copyip.length) {
    $copyip.each(function() {
      init($(this));
    });
  }
})();

//
// ClickDelete ==================================
//

var ClickDelete = (function() {
  var $clickdelete = $(".clickdelete");
  // Init
  function init($clickdelete) {
    $clickdelete.on("click", function() {
      return confirm(lang.confirm_delete);
    });
  }
  if ($clickdelete.length) {
    $clickdelete.each(function() {
      init($(this));
    });
  }
})();

//
// Broadcast ==================================
//

var Broadcast = (function () {
  var $broadcast = $(".broadcast");
  // Init
  function init($broadcast) {
    $broadcast.marquee({
      speed: 75,
      pauseOnHover: true,
    });
  }
  if ($broadcast.length) {
    $broadcast.each(function () {
      init($(this));
    });
  }
})();

$('[data-toggle="form-submit-with-loader"]').on("submit", function() {
  var form = $(this);
  var button = form.find("button[type=submit]");
  button.css('pointer-events', 'none');
  button.css('opacity', '0.5');
  button.html(lang.loading);
});

/* CONSOLE MESSAGE */
var consoleCopyrightStyle = [
  "margin: 16px 0",
  "border-radius: 10px"
].join(";");
var consoleWarningHeaderStyle = [
  "color: #ff0000",
  "font-size: 32px",
  "font-weight: 600",
  "margin: 8px 0"
].join(";");
var consoleWarningContentStyle = [
  "background-color: #ff0000",
  "color: #ffffff",
  "padding: 20px",
  "border-radius: 10px"
].join(";");
console.log(
    "%cSTOP!"+
    `%cCopyright © ${new Date().getFullYear()} LeaderOS v6`,
    consoleWarningHeaderStyle,
    consoleCopyrightStyle
);
