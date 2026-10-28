"use strict";
(function () {
	
	var _cdnProtocol = "https";
	var _cdnEndpoint = "www.termsfeed.com";
	var _plugin = "cookie-consent";
	var _version = "4.0.0";
	var _module = "cookie-consent-code.js";
	var _moduleOriginal = "cookie-consent.js";
	
	var _cdnBase = _cdnProtocol + "://" + _cdnEndpoint + "/";
	var _codeUrl = _cdnBase + "public/" + _plugin + "/" + _version + "/" + _module;
	var _pingUrl = _cdnBase + "public-ping/" + _plugin + "/" + _version + "/" + _moduleOriginal + "/" + document.location.hostname;
	
	function _nonceResolve () {
		if ((document.currentScript !== null) && (document.currentScript !== undefined)) {
			var _nonce = document.currentScript.nonce;
			if ((_nonce !== null) && (_nonce !== undefined) && (_nonce !== ""))
				return (_nonce);
		}
		var _scripts = document.getElementsByTagName ("script");
		for (var _scriptIdx in _scripts) {
			var _script = _scripts[_scriptIdx];
			if ((_script.src === null) || (_script.src === undefined))
				continue;
			if (! _script.src.startsWith (_cdnBase))
				continue;
			var _nonce = _script.nonce;
			if ((_nonce === null) || (_nonce === undefined) || (_nonce === ""))
				continue;
			return (_nonce);
		}
		return (null);
	}
	var _nonce = _nonceResolve ();
	
	var _codeElement = document.createElement ("script");
	_codeElement.async = true;
	_codeElement.src = _codeUrl;
	if (_nonce !== null)
		_codeElement.setAttribute ("nonce", _nonce);
	
	var _pingElement = document.createElement ("script");
	_pingElement.async = true;
	_pingElement.src = _pingUrl;
	if (_nonce !== null)
		_pingElement.setAttribute ("nonce", _nonce);
	
	var _applyFunctions = ["run", "i18n_enable"];
	var _applyQueue = [];
	var _applyProxy = {};
	for (var _applyFunctionIdx in _applyFunctions) {
		var _applyFunction = _applyFunctions[_applyFunctionIdx];
		(function (_applyFunction) {
				_applyProxy[_applyFunction] = function () {
					_applyQueue.push ([_applyFunction, arguments]);
				};
			} (_applyFunction));
	}
	window.cookieconsent = _applyProxy;
	_codeElement.addEventListener ("load", function () {
			if (window.cookieconsent === undefined)
				return;
			if (window.cookieconsent === _applyProxy)
				return;
			for (var _applyIdx in _applyQueue) {
				var _apply = _applyQueue[_applyIdx];
				(function (_applyFunction, _applyArguments) {
						window.setTimeout (
								function () {
									window.cookieconsent[_applyFunction].apply (null, _applyArguments);
								},
								0);
					} (_apply[0], _apply[1]));
			}
			_applyQueue = null;
			_applyProxy = null;
		});
	
	var _where = null;
	if (_where === null) _where = document.head;
	if (_where === null) _where = document.body;
	if (_where === null) _where = document;
	_where.appendChild (_codeElement);
	_where.appendChild (_pingElement);
	
} ());
