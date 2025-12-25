--Ricardo Milos
local s,id=GetID()
function s.initial_effect(c)
	--Sincro Genérico
	c:EnableReviveLimit()
	aux.AddSynchroProcedure(c,aux.FilterBoolFunction(Card.IsSetCard,0xc50),aux.NonTuner(nil),1)

end
