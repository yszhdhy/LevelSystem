import axiosInstance from "./axios-instance.ts";

type tableType = {
    id ?: number,
    img: string,
    ScaleLineDistance: string,
    tickMarksCenterPoint: string,
    bubblePlacement: string,
    bubblesDistanceHalf: string,
    bubblesCenterPoint: string,
    distance: string
    createTime ?: string
}
export default {
    async correctAtlas(img:tableType) {
        return axiosInstance.post('/save/', {
            atlas_type: 'correctAtlas',
            photo_url: img.img,
            ScaleLineDistance: img.ScaleLineDistance,
            tickMarks_center_point: img.tickMarksCenterPoint,
            bubble_placement: img.bubblePlacement,
            bubbles_distance_half: img.bubblesDistanceHalf,
            bubbles_center_point: img.bubblesCenterPoint,
            distance: img.distance,
            createTime: img.createTime
        })
    },
    async issueAtlas(img: any
    ) {
        return axiosInstance.post('/save/', {
            atlas_type: 'issueAtlas',
            photo_url: img.img,
            ScaleLineDistance: img.ScaleLineDistance,
            tickMarks_center_point: img.tickMarksCenterPoint,
            bubble_placement: img.bubblePlacement,
            bubbles_distance_half: img.bubblesDistanceHalf,
            bubbles_center_point: img.bubblesCenterPoint,
            distance: img.distance,
            createTime: img.createTime
        })
    },
    async getImgs(type: string) {
        return axiosInstance.get(`/get_list/?atlas_type=${type}`)
    },
    async deleteImg(id: number, atlasType: string) {
        return axiosInstance.get(`/delete/?id=${id}&atlas_type=${atlasType}`)
    }
}
