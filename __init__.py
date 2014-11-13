# -*- coding: utf-8 -*-
"""
/***************************************************************************
 sits_viewer
                                 A QGIS plugin
 Plugin for Satellite Image Time Series (SITS) visualization

                             -------------------
        begin                : 2014-10-27
        copyright            : (C) 2014 by Victor Maus/INPE
        email                : victor.maus@inpe.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load sits_viewer class from file sits_viewer
    from sits_viewer import sits_viewer
    return sits_viewer(iface)
