import QtQuick.Layouts 1.4
import QtQuick 2.4
import QtQuick.Controls 2.2
import org.kde.kirigami 2.4 as Kirigami
import org.kde.plasma.core 2.1 as PlasmaCore

import Mycroft 1.0 as Mycroft

Mycroft.ScrollableDelegate {
    id: delegate
//    property var restaurant
//    property var phone
//    property var location
//    property var status
//    property var url 
//    property var image_url
//    property var rating
      property var datablob
      property var restaurantModel: datablob.businesses
      backgroundImage: "https://source.unsplash.com/1920x1080/?+food"
      graceTime: 30000
    
    function getStatus(key){
        if(key){
            return "Closed"
        }
        else{
            return "Open"
        }
    }
    
    Kirigami.CardsListView{
        model: restaurantModel
        delegate: Kirigami.AbstractCard {
        id: aCard
        implicitHeight: delegateItem.implicitHeight + Kirigami.Units.largeSpacing * 3
        
        contentItem: Item {
            implicitWidth: parent.implicitWidth
            implicitHeight: parent.implicitHeight
            
        ColumnLayout {
                id: delegateItem
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                spacing: Kirigami.Units.smallSpacing
             
            Kirigami.Heading {
                id: restaurantNameLabel
                Layout.fillWidth: true
                text: modelData.name
                level: 3
                wrapMode: Text.WordWrap
            }
        
            Kirigami.Separator {
                Layout.fillWidth: true
                color: Kirigami.Theme.linkColor
            }
        
            Image {
                id: placeImage
                source: modelData.image_url
                Layout.fillWidth: true
                Layout.preferredHeight: Kirigami.Units.gridUnit * 12
                Layout.minimumHeight: Kirigami.Units.gridUnit * 12
                fillMode: Image.PreserveAspectCrop
            }
            
            Kirigami.Separator {
                Layout.fillWidth: true
                color: Kirigami.Theme.linkColor
            }
                                            
            Kirigami.FormLayout {
                id: form
                Layout.fillWidth: true
                Layout.minimumWidth: aCard.implicitWidth
                Layout.alignment: Qt.AlignLeft | Qt.AlignBottom
                                    
                Label {
                    Kirigami.FormData.label: "Location:"
                    Layout.fillWidth: true
                    wrapMode: Text.WordWrap
                    elide: Text.ElideRight
                    text: modelData.location.display_address.join(", ")
                }
                
                Kirigami.Separator {
                    Layout.fillWidth: true
                    color: Kirigami.Theme.textColor
                }
                
                Label {
                    Kirigami.FormData.label: "Phone:"
                    Layout.fillWidth: true
                    wrapMode: Text.WordWrap
                    elide: Text.ElideRight
                    text: modelData.display_phone
                }
                
                Kirigami.Separator {
                    Layout.fillWidth: true
                    color: Kirigami.Theme.textColor
                }
                
                Label {
                    Kirigami.FormData.label: "Status:"
                    Layout.fillWidth: true
                    wrapMode: Text.WordWrap
                    elide: Text.ElideRight
                    text: getStatus(modelData.is_closed)
                }
                
                Kirigami.Separator {
                    Layout.fillWidth: true
                    color: Kirigami.Theme.textColor
                }
                
                Label {
                    Kirigami.FormData.label: "Rating:"
                    Layout.fillWidth: true
                    wrapMode: Text.WordWrap
                    elide: Text.ElideRight
                    width: rater.width
                    
                    Row {
                        spacing: Kirigami.Units.largeSpacing
                        anchors.fill: parent
                    Repeater {
                        id: rater
                        model: modelData.rating
                        width: Kirigami.Units.gridUnit * 12

                        PlasmaCore.IconItem {
                            source: "star-shape"
                            implicitHeight: Kirigami.Units.gridUnit * 1.15
                            implicitWidth: Kirigami.Units.gridUnit * 1.15
                            }
                        }
                    }
                }
                
                Kirigami.Separator {
                    Layout.fillWidth: true
                    color: Kirigami.Theme.textColor
                }
            }
        }
    }
}
}
}
