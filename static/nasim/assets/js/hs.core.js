/*
 * Blueberry
 * @version: 2.0.0 (Mon, 25 Nov 2019)
 * @requires: jQuery v3.0 or later
 * @author: Nimusoft
 * @event-namespace: .HSCore
 * @license: Nimusoft Libraries ()
 * Copyright 2020 Nimusoft
 */
'use strict';

$.extend({
	HSCore: {
		init: function () {
			$(document).ready(function () {
				// Botostrap Tootltips
				$('[data-toggle="tooltip"]').tooltip();

				// Bootstrap Popovers
				$('[data-toggle="popover"]').popover();
			});
		},

		components: {}
	}
});

$.HSCore.init();